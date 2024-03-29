from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
# Models by default will have a primary key and we don't need to add them 

class car(models.Model):
    brand=models.CharField(max_length=30)
    year=models.IntegerField()


    def __str__(self):
        return f"Car is {self.brand} {self.year} and primary key is {self.pk}"


# for modelform class 
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])