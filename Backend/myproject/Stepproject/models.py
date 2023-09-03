
# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)  # You can adjust the max length as needed
    description = models.TextField(blank=True, null=True)  # Optional description field

    # Add any other fields as needed for your department model

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class StudentModel(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),

    ]
    
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    pass_hash = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    is_active = models.BooleanField(default=True)
    def _str_(self):
        return self.name



class InstructorModel(models.Model):
    InstructorID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    DateOfBirth = models.DateField(null=True, blank=True)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)
    Qualifications = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey('InstructorModel', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


