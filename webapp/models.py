from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save() #Esto tiene que estar en minusculas para que el form lo reconozca