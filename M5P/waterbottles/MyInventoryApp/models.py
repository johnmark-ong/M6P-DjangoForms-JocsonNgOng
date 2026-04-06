"""
We hereby attest to the truth of the following facts:

We have not discussed the Python code in our program with anyone
other than my instructor or the teaching assistants assigned to this course.

We have not used Python code obtained from another student, or
any other unauthorized source, whether modified or unmodified.

If any Python code or documentation used in our program was
obtained from another source, it has been clearly noted with citations in the
comments of my program.
"""

from django.db import models
from django.utils import timezone

# Create your models here.

class Supplier(models.Model):
    Name = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    Created_At = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()

    def getName(self):
        return self.Name

    def __str__(self):
        return "{}, - {}, {} created at: {}".format(self.Name, self.City, self.Country, self.Created_At)

class WaterBottle(models.Model):
    SKU = models.CharField(max_length=300)
    Brand = models.CharField(max_length=300)
    Cost = models.DecimalField(max_digits=100, decimal_places=2)
    Size = models.CharField(max_length=300)
    Mouth_Size = models.CharField(max_length=300)
    Color = models.CharField(max_length=300)
    Supplied_by = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    Current_Quantity = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return "{}: {}, {}, {}, {}, supplied by {}, {} : {}".format(self.SKU, self.Brand, self.Mouth_Size, self.Size, self.Color, self.Supplied_by, self.Cost, self.Current_Quantity)
    
class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return self.username