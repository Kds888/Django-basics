from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from . import forms
from .models import Teacher
# craete list detail update delete views are different from the template and form view 

# Create your views here.

def home_view(request):
    return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name='classroom/home.html'

class ThankYouView(TemplateView):
    template_name='classroom/thankyou.html'

class TeacherCreateView(CreateView):
    # this is a creation view, when we hit the submit button it shall create a new entry
    model=Teacher
    # as we didn't supply it with a template by default it will look under
    # model_form.html name of template in templates folder
    # and in this case it will  look at the teacher form 
    fields = '__all__' # this is a mandatory classification
    success_url = '/classroom/ty/'

class TeacherListView(ListView):
    model=Teacher
    # in this case the django will automaticcally look for model_list.html
    fields="__all__"
   # context_object_name='Teacher_list'
   # this way we can change the object_list to teacher list name in the templates 
   # here we are sending back the queryset and we can overide what we need to send by doing below steps
   # queryset=Teacher.objects.all() # this is the default what is getting back to us 
   # if we want to change it we can by chnaging the defining function of queryset like using filter 
   # queryset overites the data that will be transferred through context object name 
  
class TeacherDetailView(DetailView):
    # this class will be looking for model_detail.html
    # and this view by default requires a singular instance to be displayed accordingly
    model = Teacher
    # what detail view will do is to send a detail list of a teacher based on the primary key that they have
    # we need to find the primary key which we also have to mention in the urls   

    # for detail view you need to look at the singular instance of a teacher, here the primary key serve that purpose which is staoired in teacher.id 
    # which we can see in 0001.py in migration

class TeacherUpdateView(UpdateView):
    model = Teacher
    # this will share the model_form.html that create view also uses 
    # to update only few fields we need to define the fields
    fields=['last_name'] # for all the fields we need to supply fields with __all__ argument 
    # this allow users to update their last name only 
    success_url = '/classroom/teacher_list/' # success URL don't have .html extension they are just links 
    # we are only updating a single primary key 

class TeacherDeleteView(DeleteView):
    # it sends back a form[which contains a delete button] and requires a primary key for deletion
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')
    # default html file for this will be 
    # model_confirm_delete.html

class ContactFormView(FormView):
    form_class=forms.ContactForm # what form are we connecting it to 
    template_name='classroom/contact.html'# what URL are we sending the form to 
# what we should do after the form is submitted and 
# what to do with form 
    success_url = "/classroom/ty/"# At suceesful subission of the form which url does we have to redirect the data to 
    # suceess_url = reverse_lazy('classroom:thankyou') 
    # this we passed is th url not the .html file, as here we onl pass the url 
    def form_valid(self,form):
        # we can save this form in the models also like 
        #name = form.cleaned_data['name']
        #email = form.cleaned_data['email']
        #message = form.cleaned_data['message']
        #The cleaned_data attribute of the form instance is a dictionary containing the cleaned form data, 
        # where the keys are the names of the form fields and the values are the cleaned values entered by the user.
        return super().form_valid(form)
        # this is similar to ContactForm(request.POST)



    