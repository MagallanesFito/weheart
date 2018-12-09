from django.contrib import admin
from webapp.models import (
	UserProfile,
	Interest,
	Liked
	)
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Interest)
admin.site.register(Liked)
