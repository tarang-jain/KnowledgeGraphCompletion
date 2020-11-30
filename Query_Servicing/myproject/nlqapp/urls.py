#from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from . import views
  
urlpatterns = [ 
    path('', views.sparql_view, name='nlqapp_home' ),
    path('views.py', views.sparql_nlq, name='nlqapp_home1' ),
    path('views.py/home.html', views.sparql_nlq, name='nlqapp_home1' ),
] 