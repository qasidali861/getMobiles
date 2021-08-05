from django.db.models import Q
import requests
from bs4 import BeautifulSoup
from django.template.defaulttags import register

from django.shortcuts import render,redirect, HttpResponse ,HttpResponseRedirect,get_object_or_404
from .forms import  MobileForm, Login, ContactUsForm
from .models import  Mobile, cMobile
# Create your views here.
from django.contrib import messages
from .forms import Signup
from django.contrib.auth import authenticate,login,logout
from django.views.generic.list import ListView

def search(request):
    query = request.GET['search']
    searchMbl = cMobile.objects.filter(name__icontains = query)
    mbl = Mobile.objects.all()
    params={'searchMbl':searchMbl,'query':query,'mbl':mbl}
    return render(request,'crud/search.html',params)    



    


def sign_up(request):
    if  request.method =='POST':
        fm=Signup(request.POST)
        if fm.is_valid():
            user=fm.save()
            user.is_active = False
            user.save()
            messages.success(request,'your Account created Successfuly!!! Wait For Admin Approval')  
            return render(request,'crud/sign_up.html',{'form':fm})          
    else:
        fm=Signup()
    return render(request,'crud/sign_up.html',{'form':fm})
    

#Login views..............................................

def log_in(request):
    if  request.method =='POST':
        fm=Login(request.POST, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request , user)
                return redirect('/dashboard/')        
    else:
        fm=Login()
    return render(request,'crud/login.html',{'form':fm})
#logout view...........................................
def log_out(request):
    logout(request)
    return redirect('home')

#user Dashboard......................................
def dashboard(request):
    if  request.user.is_authenticated:
        mobile=Mobile.objects.all()
        return render(request,'crud/dashboard.html',{'mobile':mobile,'name':request.user})
    else:
        return redirect('home')
# user create mobbile view ......................................
def create(request):
    if request.user.is_authenticated:        
        if request.method == 'POST':
            form  = MobileForm(request.POST , request.FILES)
            if form.is_valid():
                
                form.save()
                return redirect('/dashboard/')
        else:
            form = MobileForm()
        return render(request, 'crud/create.html',{'form':form})    
    else:
        return redirect('home') 
# user update mobile view..........................................
def edit(request,id):
    if request.user.is_authenticated:
        mobile = Mobile.objects.get(pk=id)
        form = MobileForm(instance=mobile)
        if request.method == 'POST':
            form = MobileForm(request.POST,instance=mobile)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        return render(request,'crud/edit.html',{'form':form})
    else:
        return redirect('/dashboard/')
        #user Delete  views................ ..........
def delete(request,id): 
    if request.user.is_authenticated:
        # dictionary for initial data with  
        # field names as keys 
        context ={} 
        # fetch the object related to passed id 
        obj = get_object_or_404(Mobile, id = id) 
        if request.method =="POST": 
            # delete object 
            obj.delete() 
            # after deleting redirect to  
            # home page 
            return HttpResponseRedirect("/dashboard/") 
  
        return render(request, "crud/delete_view.html", context) 
    else:
        return redirect('/')               




def contactus(request):
    if request.method == 'POST':
            fm = ContactUsForm(request.POST)
            if fm.is_valid():
                fm.save()
            fm = ContactUsForm()
    else:
            fm = ContactUsForm()
    return render(request, 'contactus.html', {'form': fm})

def about(request):
    return render(request, 'about.html')



def home(request):
    # if request.method == "POST":
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    # form = ImageForm()
    # img = image.objects.all()
    if request.method == 'POST':
        fm = MobileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect(home)
        fm = MobileForm()
    else:
        fm = MobileForm()
        mbl = Mobile.objects.all()
        return render(request, 'home.html', {'form': fm, "mbl": mbl})

def specifications(request, link):
    mobilesH = []
    mobilesD = []
    requests.get(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')
    data = soup.find('div', {'style' : 'float:left'})  
    image = 'https://www.whatmobile.com.pk/' + data.find('img')['src']
    mobilesH.append('image')
    mobilesD.append(image)
    data1 = soup.find('td', {'class' : 'fasla RowBG1 bottom-border-section right-border specs-subHeading'})  
    price = (data1.find('strong').text).strip('\n')
    mobilesH.append('price')
    mobilesD.append(price)
    data2 = soup.find('div', {'style' : 'width:604px; vertical-align:top; margin:0 auto;'})  
    name = (data2.find('h1', {'class': 'hdng3'}).text).strip('\n')
    mobilesH.append('name')
    mobilesD.append(name)
    table = soup.find('table', class_ = 'specs')
    for i in table.find_all('th' ):
        dataH = i.text.strip()
        mobilesH.append(dataH)
    for i in table.find_all('td', {'colspan' : '2'}):
        dataD = i.text.strip()
        mobilesD.append(dataD)        
    result = dict(zip(mobilesH, mobilesD))

    return render(request, 'spec.html', {"result":result})

def mobiles(request):
    # if request.method == "POST":
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    # form = ImageForm()
    # img = image.objects.all()
    if request.method == 'POST':
        fm = MobileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            fm = MobileForm()
            return render(request, 'mobile.html', {'form': fm})
    else:
        fm = MobileForm()
        mbl = Mobile.objects.all()
        return render(request, 'mobile.html', {'form': fm, "mbl": mbl})    

def getid(request, id):
    obj = cMobile.objects.get(pk = id)
    return render(request, 'spec.html', {'obj':obj})


def oppo(request):
    url = f'https://www.whatmobile.com.pk/Oppo_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:24]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    mblD = cMobile.objects.filter(brand = 'Oppo')
    return render(request , 'oppo.html',{'oppo':Data, 'brands':mblD})
      

def samsung(request):
    url = f'https://www.whatmobile.com.pk/Samsung_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:36]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'samsung.html',{'samsung':Data})
 
def redmi(request):
    url = f'https://www.whatmobile.com.pk/Xiaomi_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:39]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'redmi.html',{'redmi':Data})

def Infinix(request):
    url = f'https://www.whatmobile.com.pk/Infinix_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:36]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'Infinix.html',{'Infinix':Data})

def Realme(request):
    url = f'https://www.whatmobile.com.pk/Realme_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:29]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'Realme.html',{'Realme':Data})

def huewei(request):
    url = f'https://www.whatmobile.com.pk/Huawei_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:19]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'huewei.html',{'huawei':Data})

def onePlus(request):
    url = f'https://www.whatmobile.com.pk/OnePlus_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('td', {'width':'668'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:17]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a')['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)

        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'oneplus.html',{'onePlus':Data})

def Tecno(request):
    url = f'https://www.whatmobile.com.pk/Tecno_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:20]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'Tecno.html',{'Tecno':Data})
    
def vivo(request):
    url = f'https://www.whatmobile.com.pk/Vivo_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('div', {'class': 'item'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:20]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a', {'class': 'BiggerText'})['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)
        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)
    return render(request , 'vivo.html',{'vivo':Data})

def Honor(request):
    url = f'https://www.whatmobile.com.pk/Honor_Mobiles_Prices'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    brands = soup.find_all('td', {'width':'668'})
    mobilesH = []
    mobilesD = []
    Data = []
    for item in brands[:17]:
        image = 'https://www.whatmobile.com.pk/' + item.find('img')['src']
        price = (item.find('span', {'class': 'PriceFont'}).text).strip('\n')
        name = (item.find('a', {'class': 'BiggerText'}).text).strip('\n')
        link = 'https://www.whatmobile.com.pk/' + item.find('a')['href']
        mobilesH.append('name')
        mobilesD.append(name)
        mobilesH.append('image')
        mobilesD.append(image)
        mobilesH.append('price')
        mobilesD.append(price)
        mobilesH.append('link')
        mobilesD.append(link)

        result = dict(zip(mobilesH, mobilesD))
        Data.append(result)

        var = 0
    
    return render(request , 'Honor.html',{'Honor':Data, 'var':var})



def under20k(request):
    under20k = cMobile.objects.filter(price__lte= 20000).order_by('-price')
    return render(request , 'under20k.html',{'under20k':under20k})

def under30k(request):
    under30k = cMobile.objects.filter(price__lte= 30000).order_by('-price')
    return render(request , 'under30k.html',{'under30k':under30k})

def under40k(request):
    under40k = cMobile.objects.filter(price__lte= 40000).order_by('-price')
    return render(request , 'under40k.html',{'under40k':under40k})

def under50k(request):
    under50k = cMobile.objects.filter(price__lte= 50000).order_by('-price')
    return render(request , 'under50k.html',{'under50k':under50k})
    



def compare(request):
    mobiles = cMobile.objects.all()
    return render(request,'compare.html', {"mobiles": mobiles})


def sidebar(request):
    mobiles = Mobile.objects.all()
    return render(request,'sidebar.html', {"mobiles": mobiles})







def compared(request):
    if request.method == "GET":
        mblss = []
        resultMbl = []
        mobile1 = request.GET.get("mobile1")
        mobile2 = request.GET.get("mobile2")
        mobile3 = request.GET.get("mobile3")
        mbl1=cMobile.objects.filter(name=mobile1).order_by('id').first()
        mbl2=cMobile.objects.filter(name=mobile2).order_by('id').first()
        mbl3=cMobile.objects.filter(name=mobile3).order_by('id').first()
        

        
        mblss.append(mbl1)
        mblss.append(mbl2)
        mblss.append(mbl3)

          
      
        for x in mblss:
            

            ramV = {
                12 : 6,
                10 : 5,
                8 : 4,
                6 : 3,
                4 : 2,
                3 : 1.5,
                2 : 1
            }
            RAM = int(x.cRAM)
            for i, j in ramV.items():
                if i == RAM:
                    bRAM = j
            

            osV = {
                11 : 5.5,
                10 : 5,
                9 : 4.5,
                8 : 4,
                7 : 3.5,
                6 : 3
            }
            OS = int(x.OS)
            for i, j in osV.items():
                if i == OS:
                    bOS = j

            gpuV = {
                'Mali' : 10,
                'PowerVR' : 15,
                'Media' : 20,
                'Adreno' : 25
            }

            for i, j in gpuV.items():
                if i == x.cGPU:
                    bGPU = j

            if x.cCPU == 'Octa Core':
                cpu1 = 8
            elif x.cCPU == 'Quad Core':
                cpu1 = 4
            pricee = int(x.price)
            if pricee <= 5000:
                bPrice = 140
            elif pricee >= 5000 and pricee <= 10000:
                bPrice = 130
            elif pricee >= 10000 and pricee <= 20000:
                bPrice = 120
            elif pricee >= 20000 and pricee <= 30000:
                bPrice = 110
            elif pricee >= 30000 and pricee <= 40000:
                bPrice = 100
            elif pricee >= 40000 and pricee <= 50000:
                bPrice = 90
            elif pricee >= 60000 and pricee <= 70000:
                bPrice = 80
            elif pricee >= 70000 and pricee <= 80000:
                bPrice = 70
            elif pricee >= 80000 and pricee <= 90000:
                bPrice = 60
            elif pricee >= 90000 and pricee <= 100000:
                bPrice = 50
            elif pricee >= 100000 and pricee <= 110000:
                bPrice = 40
            elif pricee >= 110000 and pricee <= 120000:
                bPrice = 30
            elif pricee >= 120000 and pricee <= 130000:
                bPrice = 20
            else:
                bPrice = 10
            
            battery = int(x.cBattery)

            if battery >= 500 and battery <= 1500:
                bBattery = 15
            elif battery >= 1500 and battery <= 2500:
                bBattery = 25
            elif battery >= 2500 and battery <= 3500:
                bBattery = 35
            elif battery >= 3500 and battery <= 4500:
                bBattery = 45
            elif battery >= 4500 and battery <= 5500:
                bBattery = 55
            else:
                bBattery = 60
            
            bCamera = int(x.cMainCamera) / 10 
            resultMbl.append(bRAM + cpu1  + bGPU + bOS + bPrice +  bCamera + bBattery)

        

        if resultMbl[0]==resultMbl[1] and resultMbl[1] == resultMbl[2]:
            return HttpResponse('Mobiles have same spacifiction')
        elif resultMbl[0] > resultMbl[1] and resultMbl[0] > resultMbl[2]:
            bestMobile= mbl1
        elif resultMbl[1] > resultMbl[0] and resultMbl[1] > resultMbl[2]:
            bestMobile = mbl2
        else:
            bestMobile=mbl3
        return render(request , 'compared.html',{"bestMobile":bestMobile, 'mbl1':mbl1, 'mbl2':mbl2, 'mbl3':mbl3})

from .models import Blogs

def blog(request):
    blog=Blogs.objects.all()
    return render (request,'blog.html',{'blog':blog})

  
def compareprice(request):
    mobiles = cMobile.objects.all()
    return render(request,'compareprice.html', {"mobiles": mobiles})

def showprice(request):
    if request.method == "GET":
        price1 = int(request.GET.get("price1"))
        price2 = int(request.GET.get("price2"))
        mblss=cMobile.objects.filter(price__gte=price1,price__lte=price2)
                
        if len(mblss) > 0:
            mobile_score=0
            for x in mblss:
                    ramV = {
                        12 : 6,
                        10 : 5,
                        8 : 4,
                        6 : 3,
                        4 : 2,
                        3 : 1.5,
                        2 : 1
                    }
                    RAM = int(x.cRAM)
                    for i, j in ramV.items():
                        if i == RAM:
                            bRAM = j
                    osV = {
                        11 : 5.5,
                        10 : 5,
                        9 : 4.5,
                        8 : 4,
                        7 : 3.5,
                        6 : 3
                    }
                    OS = int(x.OS)
                    for i, j in osV.items():
                        if i == OS:
                            bOS = j
                    gpuV = {
                        'Mali' : 10,
                        'PowerVR' : 15,
                        'Media' : 20,
                        'Adreno' : 25
                    }
                    for i, j in gpuV.items():
                        if i == x.cGPU:
                            bGPU = j
                    if x.cCPU == 'Octa Core':
                        cpu1 = 8
                    elif x.cCPU == 'Quad Core':
                        cpu1 = 4
                    pricee = int(x.price)
                    if pricee <= 5000:
                        bPrice = 5
                    elif pricee >= 5000 and pricee <= 10000:
                        bPrice = 10
                    elif pricee >= 10000 and pricee <= 20000:
                        bPrice = 20
                    elif pricee >= 20000 and pricee <= 30000:
                        bPrice = 30
                    elif pricee >= 30000 and pricee <= 40000:
                        bPrice = 40
                    elif pricee >= 40000 and pricee <= 50000:
                        bPrice = 50
                    elif pricee >= 60000 and pricee <= 70000:
                        bPrice = 60
                    elif pricee >= 70000 and pricee <= 80000:
                        bPrice = 80
                    elif pricee >= 80000 and pricee <= 90000:
                        bPrice = 90
                    elif pricee >= 90000 and pricee <= 100000:
                        bPrice = 100
                    elif pricee >= 100000 and pricee <= 110000:
                        bPrice = 110
                    elif pricee >= 110000 and pricee <= 120000:
                        bPrice = 120
                    elif pricee >= 120000 and pricee <= 130000:
                        bPrice = 130
                    else:
                        bPrice = 140
                    
                    battery = int(x.cBattery)

                    if battery >= 500 and battery <= 1500:
                        bBattery = 15
                    elif battery >= 1500 and battery <= 2500:
                        bBattery = 25
                    elif battery >= 2500 and battery <= 3500:
                        bBattery = 35
                    elif battery >= 3500 and battery <= 4500:
                        bBattery = 45
                    elif battery >= 4500 and battery <= 5500:
                        bBattery = 55
                    else:
                        bBattery = 60
                    
                    bCamera = int(x.cMainCamera) / 10 
                    resultMbl = (bRAM + cpu1  + bGPU + bOS + bPrice +  bCamera + bBattery)
                    if resultMbl > mobile_score:
                        mobile_score= resultMbl
                        mobile_name=x    
                
        
            return render(request , 'showprice.html',{"bestMobile":mobile_name, 'mobiles' : mblss})
    else:
        return HttpResponse("No mobile found")

