from django.urls import path
from . import views

urlpatterns = [
    path('register_user', views.register_user, name='register-user'),
    path('login_user', views.login_user, name='login-user'),
    path('logout_user', views.logout_user, name='logout-user'),
    # path('user_profile', views.user_profile, name='user-profile'),
    path('list_users', views.ListAllUsers.as_view(), name='list-users')
]
