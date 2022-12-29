from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CA(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=PhoneNumberField()
    college=models.CharField(max_length=100)
    year_of_study=models.SmallIntegerField()
    permanent_address=models.TextField()
    pincode=models.IntegerField()
    state=models.CharField(max_length=100)