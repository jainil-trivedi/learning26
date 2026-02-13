from django.shortcuts import render,redirect,HttpResponse
from .models import service
from .forms import serviceForm
# Create your views here.
def servicelist(request):
    form = service.objects.all()
    return render(request,"service/serviceList.html",{'form': form})

def serviceWithForm(request):
    if request.method == "POST":
        form = serviceForm(request.POST)
        form.save()
        return redirect("serviceList")
    else:
        form = serviceForm()
        return render(request,"service/serviceWithForm.html",{"form": form})