
from django.urls import path
from collection.views import DroneView, thanks

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', DroneView.as_view()),
    path('thanks/',views.thanks, name='thanks'),
    path('login/',views.thanks, name='login'),
]
