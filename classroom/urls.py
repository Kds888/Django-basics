from django.urls import path 
from . import views
from .views import HomeView,ThankYouView,ContactFormView,TeacherCreateView,TeacherListView,TeacherDetailView,TeacherUpdateView,TeacherDeleteView

app_name='classroom'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('ty/',ThankYouView.as_view(),name='thankyou'),
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('teacher_create/', TeacherCreateView.as_view(),name='teacher_create'),
    path('teacher_list/',TeacherListView.as_view(),name='teacher_list'),
    path('teacher_detail/<int:pk>/',TeacherDetailView.as_view(),name='teacher_detail'), # pk is primary key 
    # for detail view we need to pass the primary key as well so as to inform django which primary key we have to use 
    # these urls will look something like /classroom/teacher_detail/1/ where 1 represent primary key
    path('update_teacher/<int:pk>/',TeacherUpdateView.as_view(),name='teacher_update'),# it will by default uses create view template which is model_form.html
    path('delete_teacher/<int:pk>/',TeacherDeleteView.as_view(),name='teacher_delete'),

]