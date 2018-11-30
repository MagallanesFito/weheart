from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.forms import RegistrationForm
from django.contrib.auth.models import User 
from random import randint


''' Calcular la funcion de similitud, por lo pronto será un numero aleatorio. 
Mas tarde se opta por una funcion mas sofisticada. Esta debe tomar las preferencias de
un usuario, en forma de lista y compararlas con las preferencias del usuario logueado
en este momento, para la funcion sera request.user. De esta forma, se tiene:  

request.user : [informatics, pc, cs]  user: [plants,aeronautics]

Se calcula una similitud entre 0 y 1: Algunas opciones son: 

-entropia
-coseno. 
-word2vec

Investigar mas a detalle esta funcion. 

'''
def calculate_similarity(request,user):
	return randint(50,100)

def dashboard(request):
	users = User.objects.all()
	#actualizar este codigo mas tarde
	similarities = {}
	for user in users:
		if user != request.user:
			similarities[user] = calculate_similarity(request,user)
	return render(request,'webapp/dashboard.html',{'similarities' : similarities})
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST,request.FILES)
		#print("*"*10)
		#print(form.cleaned_data.get('profile_picture'))
		#print("*"*10)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			#user.userprofile.date_of_birth = form.cleaned_data.get('date_of_birth')
			user.userprofile.profile_picture = form.cleaned_data.get('profile_picture')
			#user.userprofile.cover_picture = form.cleaned_data.get('cover_picture')
			user.userprofile.interests = form.cleaned_data.get('interests')
			#user.userprofile.biography = form.cleaned_data.get('biography')
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