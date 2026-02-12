from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('employeeFilter/', views.employeeFilter),
    path('createEmployee/',views.createEmployee),
    path('createEmployeeForm/',views.createEmployeeWithForm,name='createEmployeeWithForm'),
    path('createCourse/',views.createCourse),
    path('Department/',views.DepartmentWithForm),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
]