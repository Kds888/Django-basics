from django.urls import path
from . import views



# register the app namespace
# URL Names
app_name ='one_one'
# this is required to use the name function of the [path] in order to transmit data to templates

urlpatterns = [
path('',views.example_view,name='example'),
path('variables/',views.variable_view,name='variable')
 
]