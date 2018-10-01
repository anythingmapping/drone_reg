from django.urls import path, re_path
from django.conf.urls import url
from collection.views import DroneReg, thanks, CameraReg
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('register_drone/', DroneReg.as_view(), name='register_drone'),
    path('registerCam/', CameraReg.as_view(), name='register_camera'),
    path('thanks/',views.thanks, name='thanks'),
    
    #login page moved to its own app
    # path('login/',views.loginView, name='loginView'),
]
