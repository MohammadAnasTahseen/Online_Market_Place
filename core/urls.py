from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path,include
from . import views

from .forms import LoginForm

urlpatterns = [
   path("",views.index,name='home'),
   path('contacts/',views.contact,name='contact'),
   path("signup/",views.signup,name='signup'),
   path("login/",auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)