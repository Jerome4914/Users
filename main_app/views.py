from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    context ={
        'users': User.objects.all(),
    }
    return render(request, "index.html", context)

def create_user(request):
    user = User.objects.create(
        first_name = request.POST['name'],
        last_name = request.POST['lname'],
        email_address = request.POST['email'],
        age = request.POST['age']
    )

    return redirect('/')
