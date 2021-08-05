from django.db import models
from django.db.models.deletion import CASCADE



class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length= 50)
    message = models.TextField(max_length=1000)

class Blogs(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    photo = models.ImageField(upload_to= "myimage")

class cMobile(models.Model):
    name = models.CharField(max_length=500,unique=True)
    image = models.CharField(max_length=500)
    price = models.IntegerField()
    brand = models.CharField(max_length=500)
    OS = models.IntegerField()
    cMainCamera = models.IntegerField()
    cRAM = models.IntegerField()
    cCPU = models.CharField(max_length=500)
    cGPU = models.CharField(max_length=500)
    cBattery = models.IntegerField()
    link = models.CharField(max_length=500)


class Mobile(models.Model):
    name = models.CharField(max_length=500,unique=True)
    image = models.CharField(max_length=500, unique=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    OS = models.IntegerField()
    cMainCamera = models.IntegerField()
    cRAM = models.IntegerField()
    cCPU = models.CharField(max_length=50)
    cGPU = models.CharField(max_length=50)
    cBattery = models.IntegerField()
    # priceCategory = models.CharField(max_length=200, 
    # choices=(
    #     ('NULL', 'NULL'),
    #     ('20000', '20000'),
    #     ('30000', '30000'),
    #     ('40000', '40000'),
    #     ('50000', '50000'),
    #     ),default= None
    # )
    Dimensions = models.CharField(max_length=500)
    Weight = models.CharField(max_length=500, default=None)
    SIM = models.CharField(max_length=500, default=None)
    Colors = models.CharField(max_length=500, default=None)
    CPU = models.CharField(max_length=500, default=None)
    Chipset = models.CharField(max_length=500, default=None)
    GPU = models.CharField(max_length=500, default=None)   
    Technology = models.CharField(max_length=500, default=None)
    Size = models.CharField(max_length=500, default=None)
    Resolution = models.CharField(max_length=500, default=None)
    Builtin = models.CharField(max_length=500, default=None)
    Card = models.CharField(max_length=500, default=None)
    Main = models.CharField(max_length=500, default=None)
    # Features = models.CharField(max_length=500, default=None)
    Front = models.CharField(max_length=500, default=None)
    WLAN = models.CharField(max_length=500, default=None)
    Bluetoth = models.CharField(max_length=500, default=None)
    Data = models.CharField(max_length=500, default=None)

    # Games = models.CharField(max_length=500, default=None)
    # Capacity = models.CharField(max_length=500, default=None)




#     gpu = models.CharField(max_length=50)
#     category = models.CharField(max_length=200, 
#     choices=(
#         ('Oppo', 'Oppo'),
#         ('Samsung', 'Samsung'),
#         ('Redmi', 'Redmi'),
#         ('iPhone', 'iPhone'),
#         ('vivo', 'vivo'),
#         ('oneplus', 'oneplus'),
#         ('lg', 'lg'),
#         ('huewei', 'huewei'),
#         ('sony', 'sony'),
#         ('nokia', 'nokia'),
#         ),default=None
#     )


#     # dOS = models.CharField(max_length=500, default=None)
#     dimensions = models.CharField(max_length=500, default=None)
    
#     # band = models.CharField(max_length=500, default=None)
    
    
   
# # protection = models.CharField(max_length=500, default=None)
    
    
#     # usb = models.CharField(max_length=500, default=None)
#     # data = models.CharField(max_length=500, default=None)
    
#     # sensors = models.CharField(max_length=500, default=None)
#     # audio = models.CharField(max_length=500, default=None)
#     # browser = models.CharField(max_length=500, default=None)




#     objects = models.Manager()
#     oppo =OppoManager()
#     samsung = SamsungManager()
#     redmi = RedMiManager()
#     iPhone = iPhoneManager()
#     vivo = vivoManager()
#     onePlus = onePlusManager()
#     huewei = hueweiManager()
#     lg = lgManager()
#     sony = sonyManager()
#     nokia = nokiaManager()
#     price20k = price20kManager()
#     price30k = price30kManager()
#     price40k = price40kManager()
#     price50k = price50kManager()
    