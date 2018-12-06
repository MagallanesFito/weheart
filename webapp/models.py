from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	date_of_birth = models.DateField(null=True)
	profile_picture = models.ImageField(default="default.jpg",upload_to='profile_picture',blank=True) #route  
	
	#cover_picture = models.ImageField(default="default_cover.png",upload_to='cover_picture') #route 
	interests = models.CharField(max_length = 1000)
	biography = models.CharField(max_length=1000,null=True)

	def __str__(self):
		return self.user.username
	'''def save(self):
		super().save()
		img = Image.open(self.profile_picture.path)

		if img.height > 300 and img.width>300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.profile_picture.path)'''
class Interest(models.Model):
	''' un usuario tiene muchos intereses'''
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save() #Esto tiene que estar en minusculas para que el form lo reconozca