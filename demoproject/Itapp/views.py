from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Itapp.models import Update
from demoproject import settings
from Itapp.forms import UserReg,UpdateUser,UpdateProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
	return HttpResponse("<h1>welcome to hello app</h1>")

def home(request):
	return render(request,'Itapp/home.html')


def about(request):
	return render(request,'Itapp/about.html')

def contact(request):
	return render(request,'Itapp/contact.html')


def register(request):
	if request.method == 'POST':
		data = UserReg(request.POST)
		if data.is_valid():
			data.save()
			return redirect('login')
		
	else:
		data=UserReg()
		return render(request,'Itapp/register.html',{'data':data})

@login_required
def dashboard(r):
	return render(r,'Itapp/dashboard.html')

@login_required
def mailsend(r):
	return render(r,'Itapp/mailsend.html')

def profile(r):
	return render(r,'Itapp/profile.html')

def update(request):
	if request.method == 'POST':
		c = UpdateUser(request.POST,instance=request.user)
		y = UpdateProfile(request.POST,request.FILES,instance=request.user.update)
		if c.is_valid() and y.is_valid():
			c.save()
			y.save()
			return redirect('profile')
	c = UpdateUser(instance=request.user)
	y = UpdateProfile(instance=request.user.update)
	return render(request,'Itapp/update.html',{'c':c,'y':y})

