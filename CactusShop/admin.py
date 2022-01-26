from django.contrib import admin

from . import models

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("Product_name",)

class ProductTypeModelAdmin(admin.ModelAdmin):
    list_display = ("ProductTypeName",)

class CustomerAccountModelAdmin(admin.ModelAdmin):
    list_display = ('Username',)

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('OrderID',)

class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ('PaymentID',)
# Register your models here.
admin.site.register(models.Product,ProductModelAdmin)
admin.site.register(models.ProductType,ProductTypeModelAdmin)
admin.site.register(models.CustomerAccount,CustomerAccountModelAdmin)
admin.site.register(models.Order,OrderModelAdmin)
admin.site.register(models.Payment,PaymentModelAdmin)