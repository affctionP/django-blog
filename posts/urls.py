from django.conf.urls import include
from django.contrib import admin
from django.urls import path ,re_path
from .views import *


app_name="posts"
urlpatterns = [
    path('', index.as_view()),
    path ('category/<slug:slug>',listofcategory,name="listed-by-cat"),
    path ('about',about,name="about_me"),

    
    #path('single', single),
    re_path(r'post/(?P<slug>[-\w]+)/',single,name="single"),
    path ('search',searchView,name= 'post_search'),
]