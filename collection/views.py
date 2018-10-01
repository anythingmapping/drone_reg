from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


from collection.models import Drone, Camera
from collection.forms import DroneForm, CameraForm

class CameraReg(TemplateView):
    template_name = 'register.html'
    
    def get(self, request):
        form = CameraForm()
        return render(request, self.template_name, {'form':form})
        
    def post(self, request):
        form = CameraForm(request.POST)
        args = {'forms': form}
        
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CameraForm()
            
        return render(request, self.template_name, args)

class DroneReg(TemplateView):
    template_name = 'register.html'
    
    def get(self, request):
        form = DroneForm()
        return render(request, self.template_name, {'form':form})
        
    def post(self, request):
        form = DroneForm(request.POST)
        args = {'forms': form}
        
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = DroneForm()
            
        return render(request, self.template_name, args)

def index(request):
    drones = Drone.objects.all()    


    return render(request, 'index.html', {'drones':drones})


def thanks(request):
    return render(request, 'thanks.html')
    
    
#Moved to accountUser

# def login(request):
#     return render(request, 'login.html')
    
# def loginView(request):
#     return render(request, 'login.html')
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return render(request, 'thanks.html')
#     else:
#         # Return an 'invalid login' error message.
#         return render(request, 'thanks.html')