

from django.contrib import admin
from django.urls import path

app_name = 'accounts'

from accounts.views import login_view, logout_view

urlpatterns = [
    path('accounts/login', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout')
]