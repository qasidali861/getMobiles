from django.contrib import admin
from .models import  Mobile, ContactUs, Blogs, cMobile
# Register your models here.

@admin.register(cMobile)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' , 'image',  'price' , 'brand', 'OS' ,'cMainCamera', 'cRAM', 'cCPU', 'cGPU', 
    'cBattery', 'link')


@admin.register(Mobile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name' ,  'price' , 'brand', 'OS' ,'cMainCamera', 'cRAM', 'cCPU', 'cGPU', 
    'cBattery', 'Dimensions', 'Weight', 'SIM', 'Colors', 'CPU','Chipset','GPU',
       'Technology',  'Size',  'Resolution',  'Builtin',
     'Card','Main',  'Front', 'WLAN', 'Bluetoth', 'Data', 'image')

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
  
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'photo')
