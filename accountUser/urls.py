
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from accountUser.views import loginView, logoutView


urlpatterns = [
    url(r'^login/', loginView, name='login'),
    url(r'^logout/', logoutView, name='logout')
]