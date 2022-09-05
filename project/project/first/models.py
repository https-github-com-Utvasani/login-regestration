from django.db import models

# Create your models here.
class Registration(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    class Meta:
        db_table="first_registration"
