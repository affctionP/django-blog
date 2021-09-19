from django.db import models
import string    
from posts.models import PostModel 

import random # define the random module  

class Subscriber(models.Model):
    email = models.EmailField(unique=True,verbose_name="ایمیل")
    created = models.DateTimeField(auto_now_add= True , verbose_name="زمان شروع دنبال کردن")
    
    confirmed = models.BooleanField(default=False,verbose_name="تایید شده")
    confirm_code = models.CharField (max_length=15,verbose_name= "کد تایید")
    #for save the id of posts every user have recived
    recived_post = models.ManyToManyField(PostModel,related_name="subscribed", verbose_name="پست های دریافتی")


    def publish_code (self):
        
        self.confirm_code= ''.join(random.choices(string.ascii_letters + string.digits, k = 15) )
        
    class Meta:
        verbose_name = "دنبال کننده"
        verbose_name_plural = "دنبال کنندگان "





