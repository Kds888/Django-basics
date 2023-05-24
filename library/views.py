from django.shortcuts import render
from . import models 
from django.views.generic import CreateView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required # decorators are used for function based views whereas 
# mixins are used for class based views
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
# it is technically a model form for user class, and we can directly use it in our views


# Create your views here.
# for user authentication on views we have 2 methods 
# 1st decorators on function based views and Mixins on class based views

def home_page(request):
    num_books =models.Book.objects.all().count()# to get the total number of books in the database
    num_instances=models.BookInstance.objects.all().count()# to count how many copies we have of the instances 
    num_instances_available = models.BookInstance.objects.filter(status__exact ='a').count()
    
    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available
    } 

    return render(request,'library/home.html',context=context)

class BookCreate(LoginRequiredMixin,CreateView): # models_form.html 
    # as the use of login required mixin will require the user to be logged_in in order to get access to this page
    model = models.Book
    fields = '__all__'
    # not mentioned about success url and by default it will go to book_detail
    success_url='/library/'
    

class BookDetail(DetailView):# one by one delivery of data 
    model=models.Book
    # error in detail view not getting displayed

@login_required # this is a decorator that will redirect and prompt the user to login, if he's not logged in.
def my_view(request):
    return render(request,'library/my_view.html')

class mysignupview(CreateView):
    form_class=UserCreationForm# overiting the built in form_class view with User creation form, generally we pass in the model
    success_url = reverse_lazy('login') # it will automatically look in project based directory login template
    template_name = 'library/signup.html'# it defines the page we are looking to connect our view with 


class checkedoutbooks(LoginRequiredMixin,ListView):# mixin will automatically direct them to the login page if the user is not logged in 
    # list all book instances and will filter according to logged in user 
    model=models.BookInstance
    template_name = 'library/profile.html'
    paginate_by = 1# this means how much data do we need to show on 1 page, means 5 books per page 

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user)# each query has a request related with it and 
        # as everry user is accessible to that request and we can filter all the books



