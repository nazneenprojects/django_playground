from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def finmarkt(request): 
    return render(request, "projects/finmarkt.html") 
  
def visualize(request): 
    return render(request, "projects/visualize.html") 
  
def about(request): 
    return render(request, "projects/about.html")
