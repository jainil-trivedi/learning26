from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username

#1 User → M Project 
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField()

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.project_name

# Project → Module : 1–M
class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=200)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "modules"

    def __str__(self):
        return self.module_name

#Module → Task : 1–M
#User → Task : 1–M
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tasks"

    def __str__(self):
        return self.task_title

#Task → Bug : 1–M
#User → Bug : 1–M
class Bug(models.Model):
    bug_id = models.AutoField(primary_key=True)
    description = models.TextField()
    status = models.CharField(max_length=50)
    reported_date = models.DateField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reported_bugs")
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_bugs")

    class Meta:
        db_table = "bugs"

    def __str__(self):
        return f"Bug {self.bug_id}"


#Task → TimeLog : 1–M
#User → TimeLog : 1–M
class TimeLog(models.Model):
    time_id = models.AutoField(primary_key=True)
    hours_spent = models.FloatField()
    log_date = models.DateField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    developer_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="time_logs")

    class Meta:
        db_table = "time_logs"

    def __str__(self):
        return f"{self.developer_id} - {self.hours_spent} hrs"

