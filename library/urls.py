from django.urls import path
from . import views

app_name='library'

urlpatterns = [
    path('',views.home_page,name='home'),
    path('create_book/',views.BookCreate.as_view(),name="create_book"),
    path('book/<int:pk>',views.BookDetail.as_view(),name='book_detail'),
    path('my_view/',views.my_view,name="my_view"),
    path('signup/',views.mysignupview.as_view(),name='signup'),
    path('profile/',views.checkedoutbooks.as_view(),name='profile'),
]
