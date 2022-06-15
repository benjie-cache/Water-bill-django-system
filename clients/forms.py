from django.forms import DateTimeInput,DateInput, ModelForm, RadioSelect,SelectDateWidget,SplitDateTimeField, SplitDateTimeWidget, TextInput, NumberInput,EmailInput
from django.forms import MultiWidget
from bootstrap_datepicker_plus.widgets import DateTimePickerInput,DatePickerInput
from django import forms
from .models import Customer
class addCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'address_line', 'metre_number','active_phone_number')
        widgets = {
            
            'full_name': TextInput(attrs=
            {
                'class': "form-control", 
                 'id':"floatingName",
                'placeholder': "Full Name"
                }),
            'address_line': TextInput(attrs=
            {
                'class': "form-control", 
                 'id':"floatingName",
                'placeholder': "Address Line"
                }),
            'metre_number': TextInput(attrs=
            {
                'class': "form-control", 
                 'id':"floatingName",
                'placeholder': "Metre Number"
                }),
             'active_phone_number': TextInput(attrs=
            {
                'class': "form-control", 
                 'id':"floatingName",
                'placeholder': "Customer PhoneNumber"
                }),
          
        }