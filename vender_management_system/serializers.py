from rest_framework import serializers
from.models import Vendor_model,Historical_Performance_Model,Purchase_order_Model

class Vendor_serializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor_model 
        fields = '__all__'

class Historical_Performance_serializers(serializers.ModelSerializer):
    class Meta:
        model = Historical_Performance_Model 
        fields = '__all__'

class Purchase_order_serializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase_order_Model 
        fields = '__all__'