from django.contrib.auth.forms import UserCreationForm
from webapp.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control', 
		'placeholder': 'Username',
		}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder': 'Password'
		}))

class RegistrationForm(UserCreationForm):
	username=forms.CharField(required=True,widget=forms.TextInput(attrs={
		'class':'form-control', 
		'placeholder': 'Username',
		}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':"Email"
		}))
	#date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	profile_picture = forms.ImageField(required=False)
	profile_picture.widget.attrs.update({'class': 'custom-file-input','id':'customFile'})
	#cover_picture = forms.ImageField(required=False)
	#cover_picture.widget.attrs.update({'class': 'custom-file-input','id':'coverPicture'})
	interests = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':"Interests ex: Science,Life,Sports",
		'id' : 'interests_text'
		}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder': 'Password'
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder': 'Repeat your password'
		}))
	#biography = forms.CharField()

	class Meta:
		model = User
		fields = [
			'username',
			#'first_name',
			#'last_name',
			'email',
			#'date_of_birth',
			'profile_picture',
			#'cover_picture',
			'interests',
			#'biography',
			'password1',
			'password2',
			]
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

