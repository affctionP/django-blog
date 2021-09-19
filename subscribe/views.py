from django.shortcuts import redirect, render
from .models import Subscriber
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

"""def SubView(request):
    if request.method == 'POST' :
        sub=Subscriber()
        sub.email=request.POST['email']
        sub.confirmed =False
        sub.publish_code()
        sub.save()
        host="http://127.0.0.1:8000/subscribe"
        subject = 'تایید آدرس ایمیل'
        message = 'سلام دوست عزیز جهت تایید آدرس ایمیل خود برای دریافت تازه ترین نوشته های من  click linke '"{}/confirm/?email={}&code={}".\
        format(host,sub.email
        ,sub.confirm_code)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [sub.email]
        send_mail( subject, message, email_from, recipient_list )
        #return HttpResponseRedirect('subscribe:send_email',request)
        return redirect(reverse('subscribe:send_email'))
        #return render(request,'index.html')


    else:
        form =subForm()
        return render(request,'index.html',{'form':form})"""

def ConfirmView(request):
    sub=Subscriber.objects.get(email=request.GET['email'])
    if sub.confirm_code == request.GET['code']:
        sub.confirmed=True
        sub.save()

    return render(request,'index.html')


def SubView(request):
    
    
    if request.method == 'POST' :
        form = SubForm(request.POST)

        sub=Subscriber()
        sub.email=request.POST['email']
        sub.confirmed =False
        sub.publish_code()
        sub.save()
        host="http://127.0.0.1:8000/subscribe"
        subject = 'تایید آدرس ایمیل'
        message = 'سلام دوست عزیز جهت تایید آدرس ایمیل خود برای دریافت تازه ترین نوشته های من  click linke '"{}/confirm/?email={}&code={}".\
        format(host,sub.email
        ,sub.confirm_code)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [sub.email]
        send_mail( subject, message, email_from, recipient_list )
        messages.add_message(request, messages.INFO, 'ایمیل تایید برای شما ارسال شد')

        
        return redirect ('/')
        
        
            
            
    else:
        form = SubForm()

    context = {
        'form': form
    }
    return render(request, 'newletter.html', context)




        
