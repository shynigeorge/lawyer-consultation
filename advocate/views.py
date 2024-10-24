# Create your views here.
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from ad_detil.models import Tbl_cat
from customer.models import DemoUser,booking,case
from .models import *


def advreg(request):
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
        exp= request.POST['experience']
        desc = request.POST['Description']
        cat = request.POST['cat']
        subc= request.POST['subcat']
        image = request.FILES['image']

        if password==conformpassword:
            if DemoUser.objects.filter(email=email).exists():
                print("email already exists")
                messages.info(request, 'email already exists')
            else:
                user = DemoUser.objects.create_user(first_name=fname, last_name=lname, email=email, password=password,
                                                username=email,is_advocate=True)
                user.save()
                customer = Tbl_adv.objects.create(u=user, Adv_fname=fname, Adv_lname=lname, Adv_email=email, Adv_gen=gend,
                                                   Adv_dob=dob,Adv_ph=mobile, Adv_city=city, Adv_state=state, Adv_dist=district,
                                                   Adv_pin=pincode, Adv_status=True, Adv_pass=password,Adv_experience=exp,Adv_image=image,Adv_description=desc,Adv_category_id=cat,Adv_subcategory_id=subc,Adv_approval=False)
                customer.save()

                return redirect('/')
    else:
        return redirect('advocate_registration')
    return render(request,'advreg.html')
                # def load_cat(request):
#     cat_id=request.GET.get('cat_id')
#     subcat=Sub_category.objects.filter(category=cat_id)
#     return render(request,'dropdown.html',{'sc':subcat})


def get_subcategories(request):
    category_id = request.POST.get('category_id')
    subcategories = Sub_category.objects.filter(category=category_id).values('id', 'sub_name')
    print(subcategories)
    return JsonResponse(list(subcategories), safe=False)

def advocate_registration(request):
    categories =Tbl_cat.objects.all()
    return render(request, 'advreg.html', {'categories': categories})


def booking_details(request):
    book = case.objects.filter(adv__u=request.user,booking__status='pending').order_by('-id')
    if request.method == 'POST':
        amt = request.POST['amount']
        id = request.POST['id']
        c = case.objects.get(id=id)
        c.booking.status='approved'
        c.booking.payment=amt
        c.booking.save()
        c.save()
        return redirect('dash')
    return render(request,'dash/bk.html',{'book':book})


# Booking Rejecting

def Booking_Rejection(request,id):
    b = booking.objects.get(id=id)
    print(b)
    b.status='rejected'
    b.save()
    print("funcvtion called")
    return redirect('advb')

