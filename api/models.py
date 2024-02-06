from django.db import models

# Create your models here.

# Creating company mode
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100, choices=(
                            ('IT', 'IT'), 
                            ('Non-IT', 'Non-IT'), 
                            ('Mobile Phones', 'Mobile Phones')
                    ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
# Creating Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.IntegerField()
    about = models.TextField()
    position = models.CharField(max_length=20,choices=(
        ('Manager', 'Manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Lead', 'Project Lead')
        ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    