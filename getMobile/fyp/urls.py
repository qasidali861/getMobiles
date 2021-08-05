"""fyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('specifications/<path:link>', views.specifications, name = "specifications"),
    path('mbl/', views.mobiles, name = 'mobiles'),
    path('<int:id>/', views.getid, name = 'getid'),
    path('oppo/',views.oppo,name='oppo'),
    path('samsung/',views.samsung,name='samsung'), 
    path('redmi/',views.redmi,name='redmi'),
    path('Infinix/',views.Infinix,name='Infinix'),
    path('vivo/',views.vivo,name='vivo'),
    path('oneplus/',views.onePlus,name='onePlus'),
    path('Tecno/',views.Tecno,name='Tecno'),
    path('Realme/',views.Realme,name='Realme'),
    path('Honor/',views.Honor,name='Honor'),
    path('huewei/',views.huewei,name='huewei'),
    path('under20k/',views.under20k,name='under20k'),
    path('under30k/',views.under30k,name='under30k'),
    path('under40k/',views.under40k,name='under40k'),
    path('under50k/',views.under50k,name='under50k'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus'),
    path('search/',views.search,name='search'),
    path('login/',views.log_in,name='log_in'),
    path('sign/',views.sign_up,name='sign_up'),

    
    path('logout/',views.log_out,name='log_out'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('create/',views.create,name='add_mobile'),
    path('delete/<int:id>',views.delete,name='delete_mobile'),

    path('edit/<int:id>',views.edit,name='edit_mobile'),
    path('compare/',views.compare,name="compare"),
    path('compared/',views.compared,name="compared"),
    path('blogs/',views.blog,name="blog"),
    path('compareprice/',views.compareprice,name="compareprice"),
    path('showprice/',views.showprice,name="showprice"),
    # path('showprice/',views.ShowMobileView.as_view(),name="showprice"),

    






 

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
