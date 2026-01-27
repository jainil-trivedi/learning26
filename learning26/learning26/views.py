from django.http import HttpResponse
from django.shortcuts import render

#specific url
def test(request):
    return HttpResponse("Hello")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactuus.html")

def home(request):
    return render(request,"home.html")

def movies(request):
    return render(request,"movies.html")

def news(request):
    return render(request,"news.html")

def show(request):
    return render(request,"show.html")