

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView , UserDetailView , UsersList

app_name = 'accounts'

urlpatterns = [
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail' ),
    path('users/', UsersList.as_view(), name='users_list' )
]