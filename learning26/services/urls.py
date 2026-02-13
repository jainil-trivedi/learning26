from . import views
from django.urls import path
urlpatterns = [
    path("serviceList/",views.servicelist),
]