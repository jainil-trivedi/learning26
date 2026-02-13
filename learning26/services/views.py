from django.shortcuts import render,redirect,HttpResponse
from .models import service
# Create your views here.
def servicelist(request):
    form = service.objects.all()
    return render(request,"service/serviceList.html",{'form': form})