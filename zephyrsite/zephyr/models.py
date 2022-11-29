from django.db import models

# Create your models here.

class CA(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.PositiveBigIntegerField(max_length=13)
    college=models.CharField(max_length=100)
    year_of_study=models.SmallIntegerField()
    permanent_address=models.TextField()
    pincode=models.IntegerField()
    state=models.CharField(max_length=100)