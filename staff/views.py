from django.shortcuts import render

# Create your views here.
from django.contrib import messages


from django.shortcuts import render, redirect

from customer.models import DemoUser
from .models import *



def staffreg(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        gend=request.POST['gender']
        dob=request.POST['dob']
        mobile=request.POST['phno']
        state=request.POST['state']
        city=request.POST['city']
        district=request.POST['dist']
        pincode=request.POST['pin']
        password= request.POST['pass']
        conformpassword=request.POST['cpass']
        if password==conformpassword:
            if DemoUser.objects.filter(email=email).exists():
                print("email already exists")
                messages.info(request, 'email already exists')
            else:
                user = DemoUser.objects.create_user(first_name=fname, last_name=lname, email=email, password=password,
                                                username=email,is_staff=True)
                user.save()
                customer = Tbl_staff(u=user, S_fname=fname, S_lname=lname, S_email=email, S_gen=gend,
                                                   S_dob=dob, S_ph=mobile, S_city=city, S_state=state, S_dist=district,
                                                   S_pin=pincode, S_status=True, S_pass=password)
                customer.save()
                messages.info(request, 'registered')
                return redirect('/')




    return render(request,'staffreg.html')


# Create your views here.
