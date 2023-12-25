from django.contrib import admin
from .models import Vendor_model,Historical_Performance_Model,Purchase_order_Model

# Register your models here.
admin.site.register(Vendor_model)
admin.site.register(Purchase_order_Model)
admin.site.register(Historical_Performance_Model)