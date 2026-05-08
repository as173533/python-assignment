from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('allpost', views.blogposts,name='allpost'),
    path('write', views.create_post, name='create-post'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('allpost/<slug:blog>', views.blog_post,name='blog-post'),
]

