from django.shortcuts import render,redirect,HttpResponse
from .models import service
from .forms import serviceForm
# Create your views here.
def servicelist(request):
    form = service.objects.all().order_by('id').values()
    return render(request,"service/serviceList.html",{'form': form})

def serviceWithForm(request):
    if request.method == "POST":
        form = serviceForm(request.POST)
        form.save()
        return redirect("serviceList")
    else:
        form = serviceForm()
        return render(request,"service/serviceWithForm.html",{"form": form})
    
def deleteservice(request,id):
    service.objects.filter(id=id).delete()
    return redirect("serviceList")

def updateservice(request,id):
    Services = service.objects.get(id=id)
    if request.method == "POST":
        form = serviceForm(request.POST, instance=Services)
        form.save()
        return redirect("serviceList")
    else:
        form = serviceForm(instance=Services)
        return render(request,"service/updateservice.html",{"form":form})    