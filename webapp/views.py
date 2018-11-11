from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.forms import RegistrationForm
from django.contrib.auth.models import User 
# Create your views here.
#def index(request):
#	return render(request,'webapp/index.html')
	#return render(request,'webapp/index.html')
def dashboard(request):
	users = User.objects.all()
	return render(request,'webapp/dashboard.html',{'users':users})
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.userprofile.date_of_birth = form.cleaned_data.get('date_of_birth')
			#user.userprofile.profile_picture = form.cleaned_data.get('profile_picture')
			#user.userprofile.cover_picture = form.cleaned_data.get('cover_picture')
			user.userprofile.interests = form.cleaned_data.get('interests')
			user.userprofile.biography = form.cleaned_data.get('biography')
			user.save()
			return redirect('/webapp')
	else:
		form = RegistrationForm()
		args = {'form':form}
	return render(request,'webapp/register.html',args)
def me(request,username=None):
	if username:
		user = User.objects.get(username=username)
	else:
		user = request.user
	separate_interests = user.userprofile.interests.replace(" ","").split(",")
	return render(request,'webapp/me.html',{'user':user,'user_interests':separate_interests})
def edit_profile(request):
	return render(request,'webapp/edit_profile.html')
def config_profile(request):
	return render(request,'webapp/config_profile.html')