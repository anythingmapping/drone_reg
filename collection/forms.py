from django import forms
from collection.models import Drone, Camera

class DroneForm(forms.ModelForm):
    
    class Meta:
        model = Drone
        fields = ['name', 'brand','serial_number','associated_camera']
        
class CameraForm(forms.ModelForm):
    
    class Meta:
        model = Camera
        fields = ['name', 'brand','megapixel']
        
