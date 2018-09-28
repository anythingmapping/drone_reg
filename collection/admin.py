from django.contrib import admin
from collection.models import Drone, Camera

class drone_admin(admin.ModelAdmin):
    model = Drone
    list_display = ('name', 'brand')

class camera_admin(admin.ModelAdmin):
    model = Camera
    list_display = ('name', 'brand')


# Register your models here.
admin.site.register(Camera, camera_admin)
admin.site.register(Drone, drone_admin)