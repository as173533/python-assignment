from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse("Home Page of our blogs")
def blogposts(request):
    return HttpResponse("All Blog Post")


# def python_intro(request):
#     return HttpResponse("Python Introduction Post")
#
# def django_basics(request):
#     return HttpResponse("Django Basics Blog Post")

def blog_post(request,blog):
    if blog == "python-basics":
        return HttpResponse("Python Basics Blog Post")
    elif blog == "django-basic":
        return HttpResponse("Django Basics Blog Post")
    elif blog == "python-opps":
        return HttpResponse("Python opps Blog Post")
    else:
        return HttpResponse(f"No Blog Post Found {blog}! ")