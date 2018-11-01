from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
	path('',views.index,name="index"), #index incluye el formulario de log in
	path('register/',views.register,name="register"),
	path('dashboard/',views.dashboard,name="dashboard"),
	path('me/',views.me,name="me")
]