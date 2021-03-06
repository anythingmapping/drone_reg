from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout)
from . forms import UserLoginForm

# Create your views here.
def loginView(request):
    print(request.user.is_authenticated)
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "login.html", {"form":form, "title": title})
    
def logoutView(request):
    logout(request)
    return redirect("/")