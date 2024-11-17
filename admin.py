from django.contrib import admin
from .models.categories import Categories
from .models.products import Products
from .models.customer import Customer
from .models.save import Save
from .models.like import Like
from message.models.message import Messagee
from message.models.project_list import Project_list

# Register your models here.


class AdminCategories(admin.ModelAdmin):
    list_display = ['name']


class AdminProducts(admin.ModelAdmin):
    list_display = ['name', 'customer', 'category','prices']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['username']


# class AdminSave(admin.ModelAdmin):
#     list_display = ['save_product_id', 'save_customer_id']


# class AdminLike(admin.ModelAdmin):
#     list_display = ['like_product_id', 'lke_customer_id', 'counter']


# class AdminMessage(admin.ModelAdmin):
#     list_display = ["reciver_id", "sender_id", "messages"]

class AdminProject_listing(admin.ModelAdmin):
    list_display = ["title",'description','email','datetime','checkpoint']


admin.site.register(Categories, AdminCategories)
admin.site.register(Products, AdminProducts)
admin.site.register(Customer, AdminCustomer)
# admin.site.register(Save, AdminSave)
# admin.site.register(Like, AdminLike)
# admin.site.register(Messagee, AdminMessage)
admin.site.register(Project_list,AdminProject_listing)