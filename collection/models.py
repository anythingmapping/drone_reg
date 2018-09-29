from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drone(models.Model):
    BRAND = (('DJI','DJI'),('PHANTOM','PHANTOM'),('x4303','x4303'))
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=21, choices=BRAND)
    serial_number = models.TextField(max_length=120)
    #PLACE HOLDER FOR CAMERA MODEL
    associated_camera = models.IntegerField()
    user = models.ForeignKey(User,None)
        
    
class Camera(models.Model):
    """ camera options """
    BRAND = (('hero3','hero3'),('12MP','12MP'),('gopro','gopro'))
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=21, choices=BRAND)
    megapixel = models.IntegerField()
    user = models.ForeignKey(User,None)
    