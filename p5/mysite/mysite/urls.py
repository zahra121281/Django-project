"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from countit import views
from countit.views import *
app_name = "countit"
urlpatterns = [
    path('form/',views.show_form),
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home_view'),
    path('breakfast/',views.breakfast,name='breakfast'),
    path('lunch_dinner/',views.lunch_dinner,name='lunch_dinner'),
    path('snack/',views.snack,name='snack'),
    path('drinks/',views.drinks,name='drinks'),
    path('dessert/',views.dessert,name='dessert'),
]

