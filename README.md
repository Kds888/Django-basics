# Django-Web Development Projects

Codes for my Django projects 

Django-Basics Project

      Project name:- one
      App name:- one_one
      
Tells us about the Simple implementation of the django template rendering with passing variables to the templates.
It has two templates named example.html and variables.html that are bieng used to tell us how to implement django functionalities on the frontend  part of things.

      App name:-office
      
 This app tells us about the way we can create models in django and how we can control user inputs through models, by the use of validators.
 It also tells us how we can imoprt the queryobject in our views and send it to our templates.
 Mentioned below are a lot of ways in which we are exploring on how and what features we can get through the use of defined variables in the models.
 
1.way of creating the actual data and storing them accordingly would be to use the command python manage.py shell 

2.and then importing the models from this class

3.from office.models import patient
4.fist way of creating it would be 
5.carl = patient(first_name ="Carl",last_name ="Smith", age=30)
6.this only cretes the object but doesn't save it and we need to save the object as well
7.carl.save() will be used here for this 
8.another method is to use the following command
9.patient.objects.create(first_name ="Carl",last_name ="Smith", age=30) and this will create an automatically save it in the database.
10.to retrieve the data we use the following command patient.objects.all()
11.this will get you all the entries that are bieng made to the patient class but in the form of query set
12.in order for us to get the real data we will be applying a str function
13.keep in mind that the indexing in the sql[database] starts from 1 not zero 
14.in the shell patient.objects.get(pk=1),it will get you the data with primary key as one and get method will only get one data field at a time
15.primary is automatically defined by django and we can see that in 0001.initial.py
16. About the Filter() command.
17.patient.objects.filter(last_name="smith").all() to sort and gather the data will all the entries with last name as smith
18.two ways to apply multiple filters 
19.patient.objects.filter(last_name="smith").filter(age=30).all() to first apply and gather the data with last name as smith and then a filter on all the smiths with age 30
20.2nd way is to use the | [or] and & [and] symbols 
21.from django.db.models import Q
22.patient.objects.filter(Q (last_name="smith") & Q (age=30)).all()
23.filed lookups is an advance way of filtering the data for example you can filter the data 
24.patient.objects.filter(last_name__startswith="s"), will only return you the data with lastnames starting with s 
25.__startswith is a field lookup and remember there is no space between the argumnet name and the filed lookup method 
26.another example would be patient.objects.filter(age__in=[10,20,30]).all()
27.this will look for age in 10,20,30 years and display the data accordingly 
28.age__gte will be age greater than or equal to  
29.in order to update an entry we can update it by refering to that entry and then calling the .save function on that for ex: -
30.carl= patient.objects.get(pk=1), will get us the data with primary key as one 
31.carl.last_name= "duke" will update it and in order to save it we will call carl.save() at end to save it for sure 
32.in order to delete an object refer it to an object and then delet that object like before we can just call carl.delete() to delete the object.
This app has only one template named list.html adn just shows us what all we can do from the use of models in our project and how we can use terminal to access and playaround with the variables.







 


