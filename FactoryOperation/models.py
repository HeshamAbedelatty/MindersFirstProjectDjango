from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, default= "hesham")
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)  # Assuming it contains email or phone number

    def __str__(self):
        return self.name
    def __str__(self):
        return self.position