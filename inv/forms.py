from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
# from .forms import Client_detail
from inv.models import *


class UserLogin(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields=['username','password', ]
        label={
            'username':'UserId',
            'password':'Password',
        }
    def __init__(self, *args, **kwargs):
        super(UserLogin,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
# class UserLogin(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client_detail
        fields = ['company_name','gst_number','country','state','address']
        
    def __init__(self, *args, **kwargs):
        super(ClientForm,self).__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs['class'] ='form-control'
        self.fields['gst_number'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Add_Service
        fields = ['client','description','quantity','amount']
       
    def __init__(self, *args, **kwargs):
        super(ServicesForm,self).__init__(*args, **kwargs)
        self.fields['client'].widget.attrs['class'] ='form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'

# add serviceprovider

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model=AddService
        fields=['client','company_name','handle_by','email','phone','account_number','ifsc_code','bank','gst_number']

    def __init__(self,*args,**kwargs):
        super(ServiceProviderForm,self).__init__(*args,**kwargs)
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['company_name'].widget.attrs['class'] = 'form-control'
        self.fields['handle_by'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['account_number'].widget.attrs['class'] = 'form-control'
        self.fields['ifsc_code'].widget.attrs['class'] = 'form-control'
        self.fields['bank'].widget.attrs['class'] = 'form-control'
        self.fields['gst_number'].widget.attrs['class'] = 'form-control'
