from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	date_of_birth = models.DateField(null=True)
	profile_picture = models.ImageField(upload_to='profile_picture',blank=True) #route  
	cover_picture = models.ImageField(upload_to='cover_picture',blank=True) #route 
	interests = models.CharField(max_length = 300)
	biography = models.TextField()

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)