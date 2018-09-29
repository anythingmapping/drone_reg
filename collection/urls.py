from django.urls import path, re_path
from django.conf.urls import url
from collection.views import DroneView, thanks, loginView, login
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', DroneView.as_view()),
    # path('registerCam/', CameraView().as_view()),
    path('thanks/',views.thanks, name='thanks'),
    
    #login page
    path('login/',views.login, name='login'),
]
