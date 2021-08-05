from django import forms
from .models import Mobile,ContactUs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__' 
        labels = {'photo': ""} 
 
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'})
 }






#login signup
class Signup(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','email','password1','password2']

        labels={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class Login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__' 
        labels = {'photo': ""}
        widgets={
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'priceCategory':forms.TextInput(attrs={'class':'form-control'}),
            'mobileName':forms.TextInput(attrs={'class':'form-control'}),
            'displaySize':forms.TextInput(attrs={'class':'form-control'}),
            'rearCamera':forms.TextInput(attrs={'class':'form-control'}),
            'batteryCapacity':forms.TextInput(attrs={'class':'form-control'}),
            'cpu':forms.TextInput(attrs={'class':'form-control'}),


            'displayResolution':forms.TextInput(attrs={'class':'form-control'}),
            'frontCamera':forms.TextInput(attrs={'class':'form-control'}),
            'drainTime':forms.TextInput(attrs={'class':'form-control'}),
            'gpu':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'dType':forms.TextInput(attrs={'class':'form-control'}),
            'screenSize':forms.TextInput(attrs={'class':'form-control'}),
            'resolution':forms.TextInput(attrs={'class':'form-control'}),

            'dimensions':forms.TextInput(attrs={'class':'form-control'}),
            'weight':forms.TextInput(attrs={'class':'form-control'}),
            'protection':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'triple':forms.TextInput(attrs={'class':'form-control'}),
            'rFeatures':forms.TextInput(attrs={'class':'form-control'}),
            'rVideo':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),


            'single':forms.TextInput(attrs={'class':'form-control'}),
            'sFeatures':forms.TextInput(attrs={'class':'form-control'}),
            'sVideo':forms.TextInput(attrs={'class':'form-control'}),
            'chipset':forms.TextInput(attrs={'class':'form-control'}),
            'card':forms.TextInput(attrs={'class':'form-control'}),
            'builtin':forms.TextInput(attrs={'class':'form-control'}),
            'usb':forms.TextInput(attrs={'class':'form-control'}),
            'battery':forms.TextInput(attrs={'class':'form-control'}),
            'technology':forms.TextInput(attrs={'class':'form-control'}),                        

            'sim':forms.TextInput(attrs={'class':'form-control'}),
            'os':forms.TextInput(attrs={'class':'form-control'}),
            'wLan':forms.TextInput(attrs={'class':'form-control'}),
            'bluetoth':forms.TextInput(attrs={'class':'form-control'}),
            'gps':forms.TextInput(attrs={'class':'form-control'}),
            'nfc':forms.TextInput(attrs={'class':'form-control'}),
            'radio':forms.TextInput(attrs={'class':'form-control'}),
            'sensor':forms.TextInput(attrs={'class':'form-control'}),
 
        } 
 
