from datetime import datetime,timedelta
from os import name
from pytz import exceptions
from rest_framework.views import Response
from .models import Historical_Performance_Model,Purchase_order_Model,Vendor_model
from rest_framework.views import APIView
from .serializers import Historical_Performance_serializers,Purchase_order_serializers,Vendor_serializers
# Purchase_order = Purchase_order_Model.objects.all()
    # Vendors_performance = Historical_Performance_Model.objects.all()
class vendors(APIView):
    
    def get(self,request,id=None):
        if id is None:
            self.vendor_detail = Vendor_model.objects.all()
            self.vendor_detail = Vendor_serializers(self.vendor_detail,many=True)
            return Response(self.vendor_detail.data, 200)
        self.vendor_detail = Vendor_model.objects.get(vendor_code = id)
        if not self.vendor_detail:
            return Response(status=204) 
        self.vendor_detail = Vendor_serializers(self.vendor_detail)
        return Response(self.vendor_detail.data, 200)
    
    def post(self,request):
        self.vendor_detail = Vendor_serializers(data=request.data)
        if self.vendor_detail.is_valid():      
            self.vendor_detail.save()
            return Response(self.vendor_detail.data, 200)
        return Response(self.vendor_detail.data,304)
    
    def put(self,request,id=None):
        self.vendor_detail = Vendor_model.objects.get(vendor_code = id)
        self.vendor_detail = Vendor_serializers(self.vendor_detail,data=request.data,partial=True)
        if self.vendor_detail.is_valid():
            self.vendor_detail.save()
            return Response(self.vendor_detail.data, 200)
        return Response(self.vendor_detail.errors,400)
    
    def delete(self,request,id):
        self.vendor_detail = Vendor_model.objects.get(vendor_code = id)
        self.vendor_detail.delete()
        return Response(status=204)



class purchase_orders(APIView):
    
    def __init__(self, *args, **kwargs):
        self.h1 = vendor_performance()
    
    def get(self,request,id=None):
        vendor = self.request.query_params.get('vendor')
        if vendor is None:
            self.order_detail = Purchase_order_Model.objects.all()
        else:
            self.order_detail = Purchase_order_Model.objects.filter(vendor = vendor)
            
        try:
            if id is None :
                self.order_detail = Purchase_order_serializers(self.order_detail,many=True)
                return Response(self.order_detail.data, 200)
            self.order_detail = Purchase_order_Model.objects.get(po_number = id)
            self.order_detail = Purchase_order_serializers(self.order_detail)
            return Response(self.order_detail.data, 200)
        except:
            return Response(status=204) 
    
    
    def post(self,request):
        self.order_detail = Purchase_order_serializers(data=request.data)
        if self.order_detail.is_valid():      
            self.order_detail.save()
            return Response(self.order_detail.data, 200)
        return Response(self.order_detail.data,304)
    
    
    def put(self,request,id):
                
        self.order_detail = Purchase_order_Model.objects.get(po_number = id)
        self.order_detail = Purchase_order_serializers(self.order_detail,data=request.data,partial=True)
        if self.order_detail.is_valid():
            self.order_detail.save()
            try:
                if request.data['status'].lower() == 'completed':
                    self.h1.quality_rating_average(id)
                    self.h1.average_response_time(id)
            except Exception as e:
                print(e)
                pass
            return Response(self.order_detail.data, 200)
        return Response(self.order_detail.errors,400)
    
    
    def delete(self,request,id):
        self.order_detail = Purchase_order_Model.objects.get(po_number = id)
        self.order_detail.delete()
        return Response(status=204)


class vendor_performance(APIView):
    def on_time_delivery(self):
        pass
    
    def quality_rating_average(self,id):
        self.data1 = Purchase_order_Model.objects.values_list('quality_rating', flat=True)
        self.data1 = [x for x in self.data1 if x != None] 
        self.data1 = sum(self.data1)/len(self.data1)
        
        
        self.change_data = Purchase_order_Model.objects.get(po_number = id)
        self.vendor_name = self.change_data.vendor
        self.change_data = Vendor_model.objects.get(name=self.vendor_name)
        self.change_data.quality_rating_avg = self.data1
        self.change_data.save()
       
        
        self.change_data = Historical_Performance_Model.objects.get(vendor = self.vendor_name)
        self.change_data.quality_rating_avg = self.data1
        self.data = datetime.now()
        self.change_data.save()
    
    def average_response_time(self,id):
        self.data1 = Purchase_order_Model.objects.values_list('issue_date','acknowledgment_date')
        self.data1=[x[1]-x[0] for x in self.data1]
        self.data1 = sum(self.data1,timedelta())/len(self.data1)
        
        
        self.change_data = Purchase_order_Model.objects.get(po_number = id)
        self.vendor_name = self.change_data.vendor
        self.change_data = Vendor_model.objects.get(name=self.vendor_name)
        self.change_data.average_response_time = self.data1
        self.change_data.save()
        
        
        self.change_data = Historical_Performance_Model.objects.get(vendor = self.vendor_name)
        self.change_data.average_response_time = self.data1
        self.data = datetime.now()
        self.change_data.save()
        
    
    def fulfillment_rate(self):
        pass
    # def get(self,request,id=None):
    #     vendor = self.request.query_params.get('vendor')
    #     if vendor is None:
    #         self.order_detail = Purchase_order_Model.objects.all()
    #     else:
    #         self.order_detail = Purchase_order_Model.objects.filter(vendor = vendor)
            
    #     try:
    #         if id is None :
    #             self.order_detail = Purchase_order_serializers(self.order_detail,many=True)
    #             return Response(self.order_detail.data, 200)
    #         self.order_detail = Purchase_order_Model.objects.get(po_number = id)
    #         self.order_detail = Purchase_order_serializers(self.order_detail)
    #         return Response(self.order_detail.data, 200)
    #     except:
    #         return Response(status=204) 
    
    
    # def post(self,request):
    #     self.order_detail = Purchase_order_serializers(data=request.data)
    #     if self.order_detail.is_valid():      
    #         self.order_detail.save()
    #         return Response(self.order_detail.data, 200)
    #     return Response(self.order_detail.data,304)
    
    
    # def put(self,request,id=None):
    #     self.order_detail = Purchase_order_Model.objects.get(po_number = id)
    #     self.order_detail = Purchase_order_serializers(self.order_detail,data=request.data,partial=True)
    #     if self.order_detail.is_valid():
    #         self.order_detail.save()
    #         return Response(self.order_detail.data, 200)
    #     return Response(self.order_detail.errors,400)
    
    
    # def delete(self,request,id):
    #     self.order_detail = Purchase_order_Model.objects.get(po_number = id)
    #     self.order_detail.delete()
    #     return Response(status=204)


