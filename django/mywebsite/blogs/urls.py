from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('allpost', views.blogposts),
    # path('allpost/python-intro', views.python_intro),
    # path('allpost/django-basic', views.django_basics),

    path('allpost/<blog>', views.blog_post),
]

