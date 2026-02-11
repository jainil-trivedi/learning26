from django import forms
from .models import Employee,Course,Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'