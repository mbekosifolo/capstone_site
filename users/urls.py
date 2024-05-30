from django.urls import path
from . import views
from .views import UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('edit_user', UserEditView.as_view(), name='edit_user'),
    path('password/', PasswordsChangeView.as_view(template_name='change_password.html')),
]
