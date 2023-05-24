from django.urls import path
from . import views

app_name='office'
# required for getting the data from the user and transfer data to the templates and in order to use the name function 

urlpatterns =[

path('',views.list_patients, name = 'list_patients')

]
