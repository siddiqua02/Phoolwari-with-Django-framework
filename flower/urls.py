from django.urls import path
from flower.views import all_flowers,flower_category,flower_details,cart,add_to_cart,remove_from_cart,check_out,place_order
urlpatterns = [
    path('all_flowers/',all_flowers,name='all_flowers'),
    path('flower_category/<int:cid>',flower_category,name='flower_category'),
    path('details/<int:id>',flower_details,name='flower_details'),
    path('cart/',cart,name='cart'),
    path("add_to_cart/",add_to_cart,name="add_to_cart"),
    path("remove_from_cart/<int:id>/",remove_from_cart,name="remove_from_cart"),
    path('check_out/',check_out,name='check_out'),
    path("place_order",place_order,name="place_order"),
    
      
]
