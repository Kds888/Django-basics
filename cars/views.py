from django.shortcuts import render,redirect
from django.urls import reverse
from . import forms 
from django.http.response import HttpResponse

from. import models
# app_name= 'cars'

# Get method requests data from a specified source
# POST method requests to send data to a server to create/update database 

# Create your views here.
 
def list_car(request):
    all_cars=models.car.objects.all()
    print(all_cars)
    # for able to send the data back to the html the data needs to be in dictionery
    context_list={"cars":all_cars}
    # this is here just to display the cars that we have added through the add car page

    return render(request,'cars/list.html',context=context_list)

def add_car(request):
    if request.POST:
        
        brand =request.POST['brand']
        year=int(request.POST['year'])
        models.car.objects.create(brand=brand,year=year)
        # the return statemnet tells us that go to the list.html page 
        return redirect(reverse('cars:listcar'))# cars: lsit is defined in urls.py where cars comes from the app name and list from the url name 
        # reverse basically says look up the cars:list and then redirect tells to redirect it to that link 
    else:
        return render(request,'cars/add.html')

def delete_car(request):
    if request.POST:
        # delete the car
        pk=request.POST['pk']# taking the data from the post method 
        try:
            models.car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:listcar'))
        except:
            print("pk not found")
            return redirect(reverse('cars:listcar'))
    else:
        return render(request,'cars/delete.html')


def rental_review(request):
    # post request -> form contents ->Thank you
    # else Render form
    if request.method=='POST':
        # checking the request method for the form, in ordee to assign operations accordingly 
        form=forms.ReviewForm(request.POST)
        # storing the data from the input from the user
        if  form.is_valid():# checking for the data in form fields whether it matches or not 
            form.save()
            return redirect(reverse('cars:thankyou'))# and if everything is fine we send the user a thank you  

    else:# else block is for first time visiting users and it will deliver them the form to fill, because they didn't fill out the form 
        form=forms.ReviewForm()# displaying the simple form on the website 
        return render(request,'cars/rental_review.html',context={'form':form})# passign the form on the html 

def thank_you(request):
    return render(request,'cars/thank_you.html')
