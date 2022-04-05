from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=100)

    phone=models.IntegerField()

    city=models.CharField(max_length=200)

    state=models.CharField(max_length=50)
    date=models.DateField()


class Client(models.Model):
    name=models.CharField(max_length=122)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    date=models.DateField()


