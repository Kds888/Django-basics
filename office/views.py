from django.shortcuts import render
from . import models 

# Create your views here.
def list_patients(request):
    all_patients=models.patient.objects.all()
    # whenever we are passig context we should remember that it should be a dictionaery
    cointext_list ={'patients':all_patients} 
    return render(request,'office/list.html',context=cointext_list )
    # provide a connection to the html file 
