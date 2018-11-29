from django.urls import path
from . import views
from django.contrib.auth.views import (
	LoginView,
	LogoutView
)

from django.conf import settings
from django.conf.urls.static import static
from webapp.forms import LoginForm


app_name = 'webapp'
urlpatterns = [
	path('',LoginView.as_view(template_name='webapp/home.html',authentication_form=LoginForm),name="home"), #index incluye el formulario de log in
	path('logout',LogoutView.as_view(template_name='webapp/logout.html'),name="logout"),
	path('register/',views.register,name="register"),
	path('dashboard/',views.dashboard,name="dashboard"),
	path('me/',views.me,name="me"),
	path('me/<str:username>',views.me,name="me_with_username"),
	path('edit/',views.edit_profile,name="edit_profile"),
	path('config/',views.config_profile,name="config_profile"),
]