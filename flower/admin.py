from django.contrib import admin

# Register your models here.

from flower.models import Category, Flower

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','seasonality', 'price', 'is_available')
    search_fields = ('name', )
    list_editable = ('is_available', )
    list_filter = ('is_available', 'category','type','seasonality')
    


admin.site.register(Category)
admin.site.register(Flower, FlowerAdmin)