from django.contrib import admin
from .models import *
from cart.models import UserOrderForm

admin.site.site_header = "Django admin panel for 'Light' site"
admin.site.register(Category)
admin.site.register(UserForm)
admin.site.register(UserOrderForm)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("email","mailing_start_date",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",),}

@admin.register(SaleItem)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",),}