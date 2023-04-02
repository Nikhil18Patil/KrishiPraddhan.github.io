"""agrogroup URL Configuration

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
from django.urls import path
from agrogroup.view import home
from agrogroup.view import contact
from agrogroup.view import product
from agrogroup.view import service
from agrogroup.view import about
from agrogroup.view import newss
from agrogroup.view import success
from agrogroup.view import goverment
from agrogroup.view import crop
from agrogroup.view import community
from agrogroup.view import whether
from agrogroup.view import marketinfo
from agrogroup.view import training
from agrogroup.view import expert
from agrogroup.view import blogone
from agrogroup.view import blogtwo
from agrogroup.view import newnews
from agrogroup.view import newdetail
from agrogroup.view import crop_form
from agrogroup.view import solution


urlpatterns = [

    path('', home,name="home"),
    path('contact/', contact,name="contact"),
    path('product/',product,name="product"),
    path('service/',service, name="service"),
    path('admin/', admin.site.urls),
    path('about/',about, name="about"),
    path('news/', newss, name="news"),
    path('success/',success,name="success"),
    path('goverment', goverment,name="goverment"),
    path('crop',crop_form,name="crop"),
    path('community',community,name="community"),
    path('weather',whether,name="weather"),
    path('marketinfo',marketinfo,name="marketinfo"),
    path('training',training,name="training"),
    path('expert',expert,name="expert"),
    path('blogone/',blogone,name="blogone"),
    path('blogtwo/',blogtwo,name="blogtwo"),
    path('newnews/',newnews,name="newnews"),
    path('new/<id>',newdetail,name="new"),
    path('solution/',solution,name="solution"),
    path('crop_form/',crop_form,name="cropform"),



  
]
