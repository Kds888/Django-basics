from django.db import models
# models are created in classes 
from django.urls import reverse
from django.contrib.auth.models import User# it gives us access to the user model

# Create your models here.
# description of the models 


class Genre(models.Model):# category of book like action,comedy
    name =models.CharField(max_length=100)
    def __str__(self):
        return self.name 
# by chance we have the same book in different language 
class Language(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=100)
    # we are connecting it to another as an author can write multiple books[one to many fields], because an author can have many book, but a book can have onlky one author
    author = models.ForeignKey('Author', on_delete=models.SET_NULL,null=True)
    # if the associated author record is deleted we just set the value to null for the books that we have stored in our database
    summary = models.TextField(max_length=600,null=True)
    isbn =models.CharField('ISBN',max_length=13,unique=True)
    genre=models.ManyToManyField(Genre)# because a book can have many categoriens and a category can be in many books
    # Here in the language we have the foriegn key relationship because the same language can have multiple books, but a book will have only one language.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk":self.pk})# pk is automatically cretaed
        # it would return the url to accesss a particular author 


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField(null=True,blank=True)# allowing for null and blank values 

    class Meta:# to dictate behaviour in admin class
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse("author_detail",kwargs={"pk":self.pk})
        # it would return the url to accesss a particular author 
    def __str__(self):
        return f"{self.last_name},{self.first_name}"


# So in total if I delete an author the book will be set to NUll in the autor field 

import uuid 

class BookInstance(models.Model):
    # assigned uniquely to every book , if the book is even a copy of the original one we still give iy unique id everytime
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)# book instance can't be deleted if there exist a book.
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null= True, blank=True)
    borrower=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)# it should be one to one as a copy can be borrowed by one user at one time 

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','Available'),
        ('r','reserved')
# custom fields for knowing the status of the book
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m')

    class Meta:
        ordering= ['due_back']# the date of return
        # odering of books will be done according to date of return  
    def __str__(self):
        return f"{self.id},{self.book.title}"
        # as book instance is connected with the book we can use the data fields define in the book as well4

    # if we are checking out a book to a user we need to associate that user to that book.

