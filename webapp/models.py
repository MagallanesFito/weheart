from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 100)
	date_of_birth = models.DateField()
	profile_picture = models.CharField(max_length = 200) #route  
	cover_picture = models.CharField(max_length = 200) #route 
	interests = models.CharField(max_length = 300)
	biography = models.TextField()

	def __str__(self):
		return self.username