
from django.urls import path
from collection.views import DroneView, thanks

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', DroneView.as_view()),
    path('thanks/',views.thanks, name='thanks'),
]
