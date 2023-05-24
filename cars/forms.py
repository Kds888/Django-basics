from django import forms
from . import models
from django.forms import ModelForm

# class ReviewForm(forms.Form):
    #first_name = forms.CharField(max_length=30,label='First Name')
    #last_name = forms.CharField(max_length=30,label='Last Name')
    # it basically generates a text input type firld in html 
   # email=forms.EmailField(label='Email')
    #review=forms.CharField(label='Please write your review ', max_length=100,widget=forms.Textarea(attrs={'class':'myform'}))
# we can only apply attributes to the widget not directly to the emailfield or charfield, we can do to them but we first need to allpy widget and then call them again 
#     email=forms.EmailField(label='Email', widget=forms.Textarea(attrs={'class':'myform'})) by this method or by editing it in the html 


# model form class 

class ReviewForm(ModelForm):
     class Meta:# we need a sublass as well, in which we define the model and fields 
        model = models.Review
        fields='__all__' # ['first_name','last_name','stars'] by mentioning in the list  we can alter the fields that we want  
        # we need to mention about the fields that we are using in this form
        # we can alter the labels in the fields by defining the dictionary named labels in the class meta 
        labels ={ 
            'first_name': 'Your First_Name'
        }
        error_message={
            'stars':{'min_value':'Your min is less than 1 ',
                    'max_value':'your max value is 5 ',}
        }