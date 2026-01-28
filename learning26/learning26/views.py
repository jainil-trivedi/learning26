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

def recipe(request):
    ingredient = ["maggie","tomato"]
    data={"name":"maggie","time":20,"ingredient":ingredient}
    return render(request,"recipe.html",data)

def team(request):
    player=["rajat patidar","venk iyer","hazlewood"]
    data={"teamname":"RCB","captain":"virat kohli","player":player,"trophy":1}
    return render(request,"team.html",data)


