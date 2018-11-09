from django.urls import path
from . import views
from django.contrib.auth.views import (
	LoginView,
	LogoutView
)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'
urlpatterns = [
	path('',LoginView.as_view(template_name='webapp/home.html'),name="home"), #index incluye el formulario de log in
	path('logout',LogoutView.as_view(template_name='webapp/logout.html'),name="logout"),
	path('register/',views.register,name="register"),
	path('dashboard/',views.dashboard,name="dashboard"),
	path('me/',views.me,name="me")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)