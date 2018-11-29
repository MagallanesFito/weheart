from django.contrib.auth.forms import UserCreationForm
from webapp.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control username_form', 
		'placeholder': 'Username',
		}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control username_form',
		'placeholder': 'Password'
		}))

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	#profile_picture = forms.ImageField()
	#cover_picture = forms.ImageField()
	interests = forms.CharField()
	biography = forms.CharField()

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'date_of_birth',
			#'profile_picture',
			#'cover_picture',
			'interests',
			'biography',
			#'password1',
			#'password2',
			)
	'''def save(self,commit=True):
		user = super(RegistrationForm,self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		#user.refresh_from_db()
		user.userprofile.date_of_birth = self.cleaned_data['date_of_birth']
		#user.userprofile.interests = self.cleaned_data['date_of_birth']
		#user.userprofile.biography = self.cleaned_data['date_of_birth']
		if commit:
			user.save()
		return user'''

