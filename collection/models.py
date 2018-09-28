from django.db import models

# Create your models here.
class Drone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
class Camera(models.Model):
    """ camera options """
    BRAND = (('hero3'),('12MP'),('gopro'))
    
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=1, choices=BRAND)
    megapixel = models.IntegerField(max_length=40)
    