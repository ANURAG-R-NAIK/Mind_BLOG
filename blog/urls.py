# CREATED BY ANURAG

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.test),
    path('', views.signup, name='signup-page'), #signup function in views
    path('loginn/', views.loginn, name='login-page'),
    path('home/', views.home, name='home-page'), # dropdown menu
    path('newpost/', views.newPost, name='new-post'),# dropdown menu
    path('mypost/', views.myPost, name='my-post'), # dropdown menu
    path('signout/', views.signout, name='signout-btn'),
    
]

#this urls.py file is then sent ti the blog_app urls.py file