from django.contrib import admin
from collection.models import Drone, Camera

class drone_admin(admin.ModelAdmin):
    model = Drone
    list_display = ('name', 'description')


# Register your models here.
admin.site.register(Camera)