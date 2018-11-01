from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'webapp/index.html')
	#return render(request,'webapp/index.html')
def dashboard(request):
	return render(request,'webapp/dashboard.html')
def register(request):
	return render(request,'webapp/register.html')
def me(request):
	return render(request,'webapp/me.html')