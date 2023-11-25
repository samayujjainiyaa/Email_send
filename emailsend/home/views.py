from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail
import random

def index(request):
    return render(request,'index.html')

def sendemail(email, otp):
    subject = "Varify Your Email Address"
    message = f"YOUR OTP IS {otp}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    print("done your otp is sent")

def generate_otp():
    return random.randint(100000, 999999)

def sendotp(request):
    if request.method == 'POST':
        email=request.POST['email']
        otp = generate_otp()
        print(email)
        print(f"Your 6-digit OTP is: {otp}")
        sendemail(email,otp)
        request.session['user_otp'] = otp
        return redirect('/varifyotp/')
    
def varifyotp(request):
    user_otp=None
    if 'user_otp' in request.session:
        user_otp = request.session['user_otp']
        print("otp stored in session",user_otp)
            
        if request.method == "POST":
            otp = request.POST['otp']
            print("you entered otp ",otp)
            if int(otp)==int(user_otp):
                request.session.clear()
                # return HttpResponse("Your Email address is verified")
                return render(request,"home.html")
            else:
                messages.info(request,"Wrong otp please try again")
                return redirect('/varifyotp/')

            # request.session.clear()
            # messages.info(request,"You attempt 3 times wrong otp please send new otp")
            # return redirect('/')
                    
    return render(request,"verifyotp.html")

