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
 
1. way of creating the actual data and storing them accordingly would be to use the command python manage.py shell 
2. and then importing the models from this class
3. from office.models import patient
4. fist way of creating it would be 
5. carl = patient(first_name ="Carl",last_name ="Smith", age=30)
6. this only cretes the object but doesn't save it and we need to save the object as well
7. carl.save() will be used here for this 
8. another method is to use the following command
9. patient.objects.create(first_name ="Carl",last_name ="Smith", age=30) and this will create an automatically save it in the database.
10. to retrieve the data we use the following command patient.objects.all()
11. this will get you all the entries that are bieng made to the patient class but in the form of query set
12. in order for us to get the real data we will be applying a str function
13. keep in mind that the indexing in the sql[database] starts from 1 not zero 
14. in the shell patient.objects.get(pk=1),it will get you the data with primary key as one and get method will only get one data field at a time
15. primary is automatically defined by django and we can see that in 0001.initial.py
16. About the Filter() command.
17. patient.objects.filter(last_name="smith").all() to sort and gather the data will all the entries with last name as smith
18. two ways to apply multiple filters 
19. patient.objects.filter(last_name="smith").filter(age=30).all() to first apply and gather the data with last name as smith and then a filter on all the smiths with age 30
20. 2nd way is to use the | [or] and & [and] symbols 
21. from django.db.models import Q
22. patient.objects.filter(Q (last_name="smith") & Q (age=30)).all()
23. filed lookups is an advance way of filtering the data for example you can filter the data 
24. patient.objects.filter(last_name__startswith="s"), will only return you the data with lastnames starting with s 
25. __startswith is a field lookup and remember there is no space between the argumnet name and the filed lookup method 
26. another example would be patient.objects.filter(age__in=[10,20,30]).all()
27. this will look for age in 10,20,30 years and display the data accordingly 
28. age__gte will be age greater than or equal to  
29. in order to update an entry we can update it by refering to that entry and then calling the .save function on that for ex: -
30. carl= patient.objects.get(pk=1), will get us the data with primary key as one 
31. carl.last_name= "duke" will update it and in order to save it we will call carl.save() at end to save it for sure 
32. in order to delete an object refer it to an object and then delet that object like before we can just call carl.delete() to delete the object.

This app has only one template named list.html adn just shows us what all we can do from the use of models in our project and how we can use terminal to access and playaround with the variables.

      App name:- cars
This app tells us about the use of forms functionality and CRUD on basic level.

Basic rules for using the Get and post request methods:-
GET:- Request Data from a sepcified source 
POST:- Request to send Data to a server.

We here have 2 types of forms:- 
Using form class and using Model forms.
Basic difference between them is that wheveevr we need to store our data to database we make use of the model form and whenver we need like a contact form we will use the forms class or we can directly use the request.post.get method to get the fields of the form and then we can use it to send an email to our desired location.

We will usually code this in forms.py of the app level, in this the code is written in the cars app.

We use the forms.FORM to define the forms through form class and add the fields as same as we define our models and In case of ModelForm we define everything in the class Meta like the name of the model and its fields, lables and error messages.

We will be passing the form to the templates and therefore we will inherit the defined form in the view.py class.

One more way of saving the data in the database is to gather the data through request.POST['data'] and then calling in the like models.car.object.create() method and is displayed in add_car view.
      
      App Name:- Classroom
Here we discuss the use of dynamic links and different available views in django.views.generic, In this we create a class and then inherit the different views that we have in the class and then we can overwrite the inherited views by defining our own variables and assigning them with our own values for example: - 
class HomeView(TemplateView):
    template_name='classroom/home.html'

These inherited views take care of the redundant task for us like saving the model form and we don't even have to use form.save or any other method for saving the details and one thing we have to take care about while using classes is when we are defining the urls of these,      path('',HomeView.as_view(),name='home'), we have to sue .as_view(), in order to pass the class as a function.

These views automatically send some context in the templates and we can acess then there directly without have to mention about them all we need is to define the model that we are using and then the fields in the model and but we have to be careful while naming the templates in our app as the templatename should be like this model_detail.html for detail view. They are also able to handle the dynamic url concept on their own.

The dynamic urls will be handled by the views[ djnago.generic.viwes ] like detailview,listview, they will handle the dynamic urls based off the id's in the database itself.
path('teacher_detail/<int:pk>/',TeacherDetailView.as_view(),name='teacher_detail'),  pk is primary key, for detail view we need to pass the primary key as well so as to inform django which primary key we have to use ,these urls will look something like /classroom/teacher_detail/1/ where 1 represent primary key.

We have to be carefull about the template names becuse based of each VIEW we have to define the template name accordingly to take benfot of these views. 

The information about different views are written in the code for view.py in classroom app.

      App Name:- Library
      
In this app we talk about various relationships that we have in the models of our class, The Inbuilt user model that can  be used from 'from django.contrib.auth.models import User', and a way of using the class meta in the models so as to dictate behaviour in the admin class.

Args:- Non keyword arguments dictated by position passing of the index.

Kwargs:- Keyword based arguments dictated by the key and value pair 

In the models here we are using the uuid as primary key for the books in the library.
Foriegn KEY defines one to many relationship. For example in the book model we have the foreign key as the autor as one author can write multiple book.
Next comes the many to many field that we use to define many to many relationships like a genre in thsi case a book an have multiple genres and a genre can have multiple books.

Here for signup we use the user creationform from inbuil functions of the django and CREATEVIEW fro djnago.views .generic to get the signup screen ready for the user to signup in our portal.

The login template is the project based template that we are using from the django inbuil templates av=n dis accessed at 'localhost 8000:accounts/login'
Here we are also using a login_required decorator[ useful for functions] along side the LOGINREQUIREDMIXIN[ useful for classes] as the use of login required mixin will require the user to be logged_in in order to get access to this page.

List view also have a variable named paginate_by that allow us to define how much data we can show on one page an dthe models can be accessed on the template like modelname_list in the template.
 Each query has a request realted with it and we can filter the books based of the given request buy the user like    
 def get_queryset(self):
 
 return models.BookInstance.objects.filter(borrower=self.request.user), each query has a request related with it and 
        
 as everry user is accessible to that request and we can filter all the books 
 
                                                                              END
 <!---------------------------------------------------------------END----------------------------------------END--------------------------------------------------->













 


