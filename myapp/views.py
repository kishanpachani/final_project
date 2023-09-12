from django.shortcuts import render,redirect,HttpResponse
from .forms import signupForm
from django.core.mail import send_mail
from kishanpachani import settings
# Create your views here.
def index(request):
    if request.method=='POST':
           newuser=signupForm(request.POST)
           if newuser.is_valid():
               newuser.save()
               print('......')
   
            # Email sending code 
               sub="WELCOME!"
               msg=f"Thank You\nFor Visiting My Portfolio "
               from_email='djangotestmail20@gmail.com'
               to_email=[request.POST['email']]
               send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
    else:
        print('error')
    return render(request,'index.html')