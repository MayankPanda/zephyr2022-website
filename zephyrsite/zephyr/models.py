from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CA(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField(unique="True")
    phone_number=models.BigIntegerField()
    college=models.CharField(max_length=100)
    year_of_study=models.SmallIntegerField()
    pincode=models.IntegerField()
    state=models.CharField(max_length=100)
    statement_of_purpose=models.TextField(default="")