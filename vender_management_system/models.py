from datetime import date
from pyexpat import model
from re import M
from django.db import models

class Vendor_model(models.Model):
    
    vendor_code = models.CharField(max_length=10,primary_key=True,unique=True)
    name = models.CharField(max_length=50,null=False)
    contact_details = models.TextField(max_length=13,null=False)
    on_time_delivery_rate = models.FloatField(null=False)     
    quality_rating_avg = models.FloatField(null=False)
    average_response_time = models.DateTimeField()
    fulfillment_rate = models.FloatField(null=False)
    
    def __str__(self) -> str:
        return self.name
    
class Purchase_order_Model(models.Model):
    
    po_number = models.CharField(max_length=10,primary_key=True,null=False,unique=True)
    vendor = models.ForeignKey(Vendor_model, on_delete= models.CASCADE,null=False)
    order_date = models.DateTimeField(null=False)
    delivery_date = models.DateTimeField(null=False)
    items = models.JSONField(null=False)
    quantity = models.IntegerField(null=False)
    status = models.CharField(max_length=10,null=False)
    quality_rating = models.FloatField(default=0.0,blank=True,null=True)
    issue_date = models.DateTimeField(null=False)
    acknowledgment_date = models.DateTimeField(null=False)
    
    def __str__(self) -> str:
        return self.po_number
    
class Historical_Performance_Model(models.Model):
    
    vendor = models.ForeignKey(Vendor_model, on_delete= models.CASCADE,primary_key=True,unique=True)
    date = models.DateTimeField(null=False)
    on_time_delivery_rate = models.FloatField(null=False)
    quality_rating_avg = models.FloatField(null=False) 
    average_response_time = models.DateTimeField()
    fulfillment_rate = models.FloatField(null=False)
    