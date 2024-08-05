from django.shortcuts import render,redirect,get_object_or_404
from flower.models import Flower,Category,Order
from user.models import Address

from django.conf import settings
from django.core.mail import send_mail


from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import time,date,timedelta
# Create your views here.

def all_flowers(request):
    flowers = Flower.objects.all()
    categories = Category.objects.all().order_by('category')
    # print(flowers.query)
    context = {
        "flowers" : flowers,
        "categories" : categories,
    }
    print(categories)
    return render(request, "page/all_flowers.html", context)

def flower_category(request,cid):
    flowers=Flower.objects.filter(category=cid)
    categories=Category.objects.all().order_by('category')
    # print(flowers.query)
    context={
        "flowers":flowers,
        "categories":categories
    }
    #print(categories)
    return render(request,"page/all_flowers.html",context)

def flower_details(request,id):
    #flower=Flower.objects.get(id=id)
    flower=get_object_or_404(Flower,id=id)
    quantity=1
    if request.session.get("cart_items"):
        if request.session.get('cart_items').get(str(id)):
            quantity=request.session.get("cart_items")[str(id)]
    context={
        'flower':flower,
        'quantity':quantity
    }
    return render(request,"flower/flower_details.html",context)

def get_cart_details(request):
    cart_items=request.session.get('cart_items')
    if cart_items is None:
        cart_items={}
    flowers=Flower.objects.filter(id__in=list(cart_items.keys()))
    total_price=0
    cart_details=[]
    for flower in flowers:
        quantity=int(cart_items[str(flower.id)])
        price=quantity*flower.price
        total_price+=price
        cart_details.append({
            "id":flower.id,
            "name":flower.name,
            "quantity":quantity,
            "price":price,
            "image":flower.image
                
        })
    return cart_details,total_price

def cart(request):
    cart_details,total_price =get_cart_details(request)
    context={
        "flowers":cart_details,
        "total_price":total_price
    }
    return render(request,"flower/cart.html",context)

def add_to_cart(request):
    if request.method=="POST":
        flower_id=request.POST.get("flower_id")
        quantity=request.POST.get("quantity")
        cart_items={}
        if request.session.get("cart_items"):
            cart_items=request.session.get("cart_items")
        cart_items[flower_id]=quantity
        request.session["cart_items"]=cart_items
        print(request.session.get("cart_items"))
    return redirect("cart")

def remove_from_cart(request,id):
    cart_items=request.session.get('cart_items')
    del cart_items[str(id)]
    request.session['cart_items']=cart_items
    return redirect('cart') 


def check_out(request):
    addresses=Address.objects.filter(user=request.user)
    cart_details,total_price=get_cart_details(request)
    context={
        "addresses":addresses,
        "flowers":cart_details,
        'total_price':total_price
    } 
    return render(request,'page/check_out.html',context)

def place_order(request):
    if request.method=="POST":
        user=request.user
        address=request.POST.get("address")
        address=Address.objects.get(id=address)
        payment_mode=request.POST.get('payment_mode')
        cart_details,total_price=get_cart_details(request)
        orders=[]
        for flower in cart_details:
            order = Order(
                flower = Flower.objects.get(id=flower['id']),
                user = user,
                address = address,
                quantity = flower['quantity'],
                price = flower['price'],
                payment_method = payment_mode
            )
            orders.append(order)
    Order.objects.bulk_create(orders)
    
    subject="Order placed sucesssfully"
    mail_context={
        "username":request.user.first_name+" "+request.user.last_name,
        "flowers": cart_details,
        "addresss":address,
        "delivery_date": date.today() + timedelta(days=2),
        "total_price":total_price
    }
    html_message=render_to_string('flower/mail_template.html',mail_context)
    plain_message=strip_tags(html_message)
    #body=f"Your Order is placed sucessfully. Amount {total_price}.Delivery address:{address}"
    to=[request.user.email,]
    from_email=settings.EMAIL_HOST_USER
    #send_mail(subject=subject,message=body,from_email=from_email,recipient_list=to,fail_silently=False)
    send_mail(subject=subject,message=plain_message,from_email=from_email,recipient_list=to,fail_silently=False)
    request.session['cart_items']={} 
    return render(request,"page/ThankYou.html",mail_context)