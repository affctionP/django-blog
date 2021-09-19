from django.dispatch.dispatcher import receiver
from .models import PostModel
from django.db.models.signals  import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from subscribe.models import Subscriber
from django.utils import timezone
@receiver(post_save,sender=PostModel)
def send_email(sender,instance,**kwargs):
    
    subs= Subscriber.objects.filter(confirmed =True)
    print (instance.updated)
    print (instance.publish)
    if instance.status == 'p' and instance.updated.strftime('%Y-%m-%d') == instance.publish.strftime('%Y-%m-%d'):
        lists={}
        for e in subs:
            lists[e.email]=[]
            for recive in  e.recived_post.all():
               lists[e.email].append(recive)
            
            
            
            if instance  not in lists[str(e.email)]:
                subject = 'welcome to GFG world'
                message = 'http://127.0.0.1:8000/post/{}'.format(instance.slug)
                email_from = settings.EMAIL_HOST_USER
                recipient_list=[e.email]
                send_mail( subject, message, email_from, recipient_list )
                e.recived_post.add(instance)


        



