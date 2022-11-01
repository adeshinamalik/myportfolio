from django.shortcuts import redirect, render
from django.contrib import messages
from .models import info
# Create your views here.

def index(request):
    return render(request, 'index.html')

def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        information = info(name=name, email=email, message=message)
        information.save()
        return redirect('message')
    else:
        return render(request, 'index.html')