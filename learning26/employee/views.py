from django.shortcuts import render
from .models import Employee
# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all() #select * from employee 
    employees = Employee.objects.all().values()
    #employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/employeeList.html',{"employees":employees})

def employeeFilter(request):
    #where select  from employee where name = "raj"
    employee = Employee.objects.filter(name ="raj").values()
    #selet  from employee where post = "Tester"
    employee1 = Employee.objects.filter(post="Tester").values()
    #select  from employee where name = "dhruv" and post = "Tester"
    employee2 = Employee.objects.filter(name="dhruv",post="Tester").values()

    #seelct  from employee where age > 23
    #employee4 = Employee.objects.filter(age>23).values()
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values() #__gte mean greater than equal

    #string queries
    employee6 = Employee.objects.filter(post__exact="Tester").values()
    employee7 = Employee.objects.filter(post__iexact="tester").values()

    #contains
    employee8 = Employee.objects.filter(name__contains="d").values()
    employee9 = Employee.objects.filter(name__icontains="D").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

    #in
    employee14 = Employee.objects.filter(name__in=["raj","jay"]).values()   

    #range
    employee15 = Employee.objects.filter(age__range=[22,30]).values() 

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc






    print("query 1",employee)
    print("query2",employee1)
    print("query3",employee2)
    print("query 4",employee4)
    print("query5",employee5)
    print("query6",employee6)
    print("query7",employee7)
    print("query8",employee8)
    print("query9",employee9)
    print("query10",employee10)
    print("query11",employee11)
    print("query12",employee12)
    print("query13",employee13)
    print("query14",employee14)
    print("query15",employee15)
    print("query16",employee16)
    print("query17",employee17)
    return render(request, 'employee/employeeFilter.html')