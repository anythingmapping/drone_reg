from django import forms
from collection.models import Drone

class DroneForm(forms.ModelForm):
    
    
    class Meta:
        model = Drone
        fields = ['name', 'brand','serial_number','associated_camera']
        
