from . import views
from django.urls import path
urlpatterns = [
    path("serviceList/",views.servicelist,name="serviceList"),
    path("serviceWithForm/",views.serviceWithForm,name="serviceWithForm"),
    path("deleteservice/<int:id>",views.deleteservice,name = "deleteservice"),
    path("updateservice/<int:id>",views.updateservice,name="updateservice"),
]