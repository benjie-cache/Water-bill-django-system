from django.shortcuts import render
from .forms import addCustomerForm
from django.views.generic.list import ListView
from .models import Customer ,WaterBilling
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    client_list=Customer.objects.all().order_by('id')
    first_client=client_list[0]
    first_client_id=first_client.pk
   
    context={"first_client_id":first_client_id}
    return render(request, 'dashboard.html',context)
class  CustomerList(ListView):
    model=Customer
    context_object_name='customers'
    template_name='dashboard.html'
class CustomerCreate(CreateView):
    
    model=Customer
    template_name='customer_form.html'
    success_url=reverse_lazy('home')
    form_class=addCustomerForm
   
    
    def form_valid(self,form):
       
        return super(CustomerCreate,self).form_valid(form)
class CustomerDelete(DeleteView):
    model= Customer
    context_object_name='customer'
    template_name='confirm_delete.html'
    success_url=reverse_lazy('home')    
class CustomerUpdate(UpdateView):
    model=Customer
    form_class=addCustomerForm
    template_name='customer_form.html'
    
    success_url=reverse_lazy('home')


##############invoices
def invoice_template(request,pk):
    customer_billing=WaterBilling.objects.get(customer=pk)
    customer_details=Customer.objects.get(id=pk)
    clients=Customer.objects.all()
    
    current_time=datetime.now()
    today_date="{}/{}/{}".format(current_time.day,current_time.month,current_time.year)
    context={ "customer_billing":customer_billing,"today_date":today_date,
             "customer_details":customer_details,"clients":clients}
    return render(request, 'invoice_template.html',context)
    
    