
from django.shortcuts import render,redirect
from.models import Service
from .forms import ServiceForm
# Create your views here.

def studentHome(request):
    return render(request,"studentHome.html")

def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student)    
                           #student/studentDashboard.html
                           #folder/filename

def studentmarks(request):
    marks={"het":70,"zeel":58,"jay":56}
    return render(request,"student/studentmarks.html",marks)

def studentid(request):
    id={"het":101,"zeel":102,"jay":103}
    return render(request,"student/studentid.html",id)

def servicelist(request):
    services = Service.objects.all()
    return render(request,"student/servicelist.html",{"services": services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})