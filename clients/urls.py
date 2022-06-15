from django.urls import  path
from .views import CustomerDelete, CustomerList,CustomerCreate, CustomerUpdate
from . import views
urlpatterns = [
    path('', CustomerList.as_view(), name='home'),
    path('add-customer/', CustomerCreate.as_view(), name='add-customer'),
    path('delete-customer/<slug:slug>', CustomerDelete.as_view(), name='delete-customer'),
    path('edit-customer/<slug:slug>', CustomerUpdate.as_view(), name='edit-customer'),
    
    ########invoice handling#####
    path('invoice_template/<int:pk>',views.invoice_template,name='invoice')
    
   
]