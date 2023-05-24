from django.urls import path
from . import views

app_name= 'cars'

urlpatterns = [

path('list/',views.list_car,name='listcar'),
path('add/',views.add_car,name='addcar'),
path('delete/',views.delete_car,name='deletecar'),
path('rr/',views.rental_review,name='rentalreview'),
path('thankyou/',views.thank_you,name='thankyou')

]
# path expects a function to be passed in it.
