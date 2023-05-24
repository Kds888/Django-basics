"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
# through redirect view we can redirect the request to another url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('one_one/',include('one_one.urls')),
    path('office/',include('office.urls')),
    path('cars/',include('cars.urls')),
    path('classroom/', include('classroom.urls')),
    path('library/',include('library.urls')),
    path('',RedirectView.as_view(url='library/')),
    # this will make the home page to redirect to the library page url 
    path('accounts/',include('django.contrib.auth.urls'))# they are already setup in the django for us 
    # it will add the urls like login logout password change password change done password reset password reset done password reset confirm 
    # password resert complete 
    # and we can acess them like accounts / login/ etc 
    # models and views will be created using this but we need to still create a template file for login and logout pages
    # in order to access these pages we will need to pass create a new folder named registration under templates on site level production
    # and then configure it in settings

]

# handler404='one.views.custom_error_page'
# django specifically looks for handler to display our views
# but if we are using 404.html we don't need it 