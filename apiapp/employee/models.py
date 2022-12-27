from django.db import models

# Create your models here.


class Employee(models.Model):
    Name = models.CharField(max_length=25)
    email = models.EmailField()
    eid = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"
