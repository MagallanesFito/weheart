from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.forms import RegistrationForm
from django.contrib.auth.models import User 
import random
from webapp.models import Interest,Liked
import requests
import json


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
def jaccard_similarity(actual_user,user):
	#Similitud de Jaccard
	request_user_list = actual_user.userprofile.interests.split(",")[:-1]
	user_list = user.userprofile.interests.split(",")[:-1]
	set_request = set(request_user_list)
	set_user = set(user_list)
	similarity = (len(set_request & set_user)/len(set_user | set_request))
	return similarity
	return float("{0:.2f}".format(similarity)) 
	#return randint(50,100)
def semantic_similarity(actual_user,user):
	'''token = "<YOUR_TOKEN_HERE>"
	url = "https://api.dandelion.eu/datatxt/sim/v1/"
	texto1 = actual_user.userprofile.biography
	texto2 = user.userprofile.biography
	dict_data = {"text1": texto1, "text2" : texto2,"lang" : "en", "token" : token}
	dict_data = json.dumps(dict_data)
	loaded_r = json.loads(dict_data)
	r = requests.post(url, data=loaded_r)
	return (r.json()['similarity'])'''
	return random.uniform(0.5, 1)
def calculate_similarity(actual_user,user):
	
	result_semantic = semantic_similarity(actual_user,user)
	result_jaccard = jaccard_similarity(actual_user,user)
	#Se da menor importancia a jaccard que a semantico,
	#revisar esta metrica para despues
	resultado = (0.3*result_jaccard+0.7*result_semantic)*100
	return float("{0:.2f}".format(resultado))  
	

def dashboard(request):
	#users = User.objects.all()
	users = User.objects.exclude(pk=request.user.pk)

	try:
		friend = Liked.objects.get(current_user=request.user)
		friends = friend.users.all()
	except Liked.DoesNotExist:
		friends = []
	#actualizar este codigo mas tarde
	similarities = {}
	actual_user = request.user
	#La consulta debe ser excluyendo el usuario actual
	for user in users:
		#if user != request.user:
		similarities[user] = calculate_similarity(actual_user,user)
	ordenado = dict(sorted(similarities.items(),key=lambda kv : kv[1],reverse=True))
	return render(request,'webapp/dashboard.html',{'similarities' : ordenado,'friends':friends})
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
			user.userprofile.cover_picture = form.cleaned_data.get('cover_picture')
			user.userprofile.interests = form.cleaned_data.get('interests')
			user.userprofile.biography = form.cleaned_data.get('biography')
			if user.userprofile.biography == "":
				user.userprofile.biography = "Hey there, I'm using weHeart to make some friends"
			user.save()
			return redirect('/webapp')
	else:
		form = RegistrationForm()
		query = Interest.objects.all()
		list_interests = []
		for element in query:
			list_interests.append(element.name)
		args = {'form':form,'list_interests':list_interests}
		return render(request,'webapp/register.html',args)
def me(request,username=None):
	if username:
		user = User.objects.get(username=username)
	else:
		user = request.user
	separate_interests = user.userprofile.interests.split(",")[:-1]
	is_friend = False
	local_friends = None
	#Likes del perfil que se visita
	try:
	    friend = Liked.objects.get(current_user=user)
	    friends = friend.users.all()
	except Liked.DoesNotExist:
	    friends = []
	#Likes del perfil visitante
	if user != request.user:
		try:
			local_friend = Liked.objects.get(current_user=request.user)
			try:
				local_friends = local_friend.users.get(username=user.username)
			except User.DoesNotExist:
				local_friends = None
		except Liked.DoesNotExist:
			local_friends = None
	if local_friends != None:
		is_friend = True
	args = {'user':user,
	'user_interests':separate_interests,
	'friends' : friends,
	'is_friend':is_friend}
	return render(request,'webapp/me.html',args)
def edit_profile(request):
	return render(request,'webapp/edit_profile.html')
def config_profile(request):
	return render(request,'webapp/config_profile.html')
def like_profile(request,operation,pk,source,destination):
	new_friend = User.objects.get(pk=pk)
	if operation=='add':
		Liked.like_profile(request.user,new_friend)
	elif operation=='remove':
		Liked.dislike_profile(request.user,new_friend)
	if source=='me_with_username':
		return redirect('webapp:me_with_username',username=destination)
	elif source == 'dashboard':
		return redirect('webapp:dashboard')