from django.http import HttpResponse

# Create your views here.
def blogs(request):
    return HttpResponse("Hello World")