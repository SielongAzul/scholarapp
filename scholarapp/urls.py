from django.urls import path
from . import views




#This is where the urls are supposed to be installed

urlpatterns = {
    path('', views.home, name="Home"),
    
    
}