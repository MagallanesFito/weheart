from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.forms import RegistrationForm
# Create your views here.
#def index(request):
#	return render(request,'webapp/index.html')
	#return render(request,'webapp/index.html')
def dashboard(request):
	return render(request,'webapp/dashboard.html')
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/webapp')
	else:
		form = RegistrationForm()
		args = {'form':form}
		return render(request,'webapp/register.html',args)
def me(request):
	return render(request,'webapp/me.html')