from django.contrib import admin
from .models import Customer,WaterMeter,WaterBilling,WaterConsumption,WaterPayments
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'address_line', 'metre_number', 'active_phone_number']
    list_filter = ['full_name',]
    search_fields = ['metre_number',]
@admin.register(WaterMeter)    
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ['meter_number', 'custom_er', 'created', 'updated']
    list_filter = ['meter_number',]
    search_fields = ['metre_number',]
@admin.register(WaterBilling)    
class WaterBillingAdmin(admin.ModelAdmin):
    list_display = ['bill_code', 'meter_number', 'units', 'unit_price','total','amount_paid','month','cleared','from_date'
                    ,'to_date','due_date']
    list_filter = ['bill_code',]
    search_fields = ['metre_number','bill_code']    
   
@admin.register(WaterConsumption)    
class WaterConsumptionAdmin(admin.ModelAdmin):
    list_display = ['parent','previous_reading','current_reading','consumption','reading_added']
    list_filter = ['parent',]
    search_fields = ['parent']    
@admin.register(WaterPayments)    
class WaterPaymentsAdmin(admin.ModelAdmin):
    list_display = ['parent','tracking_code','amount','payment_method','status']
    list_filter = ['parent',]
    search_fields = ['parent']         
