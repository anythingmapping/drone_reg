from django import forms
from collection.models import Drone

class DroneForm(forms.Form):
    hello = forms.CharField()
    ello = forms.CharField()
