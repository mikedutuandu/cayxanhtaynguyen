from django.contrib import admin

# Register your models here.


from .models import UserCheckout, Order
from apps.accounts.models import UserAddress


admin.site.register(UserCheckout)


admin.site.register(UserAddress)

admin.site.register(Order)