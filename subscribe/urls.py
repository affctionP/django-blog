from django.urls import path
from django.urls.resolvers import URLPattern
from .views import  *
from django.urls import path

app_name ="subscribe"
urlpatterns =[
    path('add',SubView,name='send_email'),
    path('confirm/',ConfirmView,name='confirm'),
    #path('remove'),
    


]