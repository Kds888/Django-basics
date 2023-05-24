from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# these are validators that will control the inputs from the user, for example a user cannot put the heartrate to be 0.

# Create your models here.


class patient(models.Model):
    # here the databse is defined through classes 
    first_name=models.CharField(max_length=30)
    # defining a coloumn in the databse 
    last_name=models.CharField(max_length=30)
    age=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    # as existing patients don't have any heart rate values, django will give us a warning when we run makemigrations command 
    heartrate=models.IntegerField(default=60,validators=[MinValueValidator(1), MaxValueValidator(280)]), # these are in order to avoid typos


    def __str__(self):
        # this function will give us human readable data instaed of query sets data
        return f"{self.first_name},{self.last_name} is {self.age} years old."
# way of creating the actual data and storing them accordingly would be to use the command python manage.py shell 
# and then importing the models from this class
# from office.models import patient
# fist way of creating it would be 
# carl = patient(first_name ="Carl",last_name ="Smith", age=30)
# this only cretes the object but doesn't save it and we need to save the object as well
# carl.save() will be used here for this 
# another method is to use the following command
# patient.objects.create(first_name ="Carl",last_name ="Smith", age=30) and this will create an automatically save it in the databse

# to retrieve the data we use the following command patient.objects.all()
# this will get you all the entries that are bieng made to the patient class but in the form of query set
# in order for us to get the real data we will be applying a str function
# keep in mind that the indexing in the sql starts from 1 not zero 

# in the shell patient.objects.get(pk=1),it will get you the data with primary key as one and get method will only get one data field at a time
# primary is automatically defined by django and we can see that in 0001.initial.py 

# filter()
# patient.objects.filter(last_name="smith").all() to sort and gather the data will all the entries with last name as smith
# two ways to apply multiple filters 
# patient.objects.filter(last_name="smith").filter(age=30).all() to first apply and gather the data with last name as smith and then a filter on all the smiths with age 30
# 2nd way is to use the | [or] and & [and] symbols 
# from django.db.models import Q
# patient.objects.filter(Q (last_name="smith") & Q (age=30)).all()
# filed lookups is an advance way of filtering the data for example you can filter the data 
# patient.objects.filter(last_name__startswith="s"), will only return you the data with lastnames starting with s 
# __startswith is a filed lookup and remember there is no space between the argumnet name and the filed lookup method 
# another example would be patient.objects.filter(age__in=[10,20,30]).all()
# age__gte will be age greater than or equal to  
# this will look for age in 10,20,30 years and display the data accordingly 

# in order to update an entry we can update it by referingh to that entry and then calling the .save function on that for ex: -
# carl= patient.objects.get(pk=1), will get us the data with primary key as one 
# carl.last_name= "django" will update it and in order to save it we will call carl.save() at end to save it for sure 

# in order to delete an object refer it to an object and then delet that object like before we can just call carl.delete() to delete the object

