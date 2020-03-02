from django.contrib import admin
from .models import ProductDetail,Contact,Orders, orderUpdate

# Register your models here.

admin.site.register(ProductDetail)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(orderUpdate)
