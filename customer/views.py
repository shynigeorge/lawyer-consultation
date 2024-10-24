from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
from django.shortcuts import render, redirect,HttpResponse
from django.utils import timezone
from django.views import View

from ad_detil.models import Sub_category, Tbl_cat
from advocate.models import Tbl_adv
from staff.models import Tbl_staff
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa
from io import BytesIO



def home(request):
    adv=Tbl_adv.objects.all()

    cat=Tbl_cat.objects.all()

    subcat=Sub_category.objects.all()

    return render(request,'index.html',{"adv":adv})

def Cases_show(request):
    cat=Tbl_cat.objects.all()

    subcat=Sub_category.objects.all()
    return render(request,'cases.html',{'cat':cat,'scat':subcat})

def loginpage(request):

    if request.method == 'POST':
        username=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                print('super user')
                return redirect('dash')
            elif request.user.is_staff:
                st =  Tbl_staff.objects.get(u=user)
                if st.S_status==True:
                    print('staff')
                    return redirect('dash')
                else:
                    return redirect('adv')

            elif request.user.is_advocate:
                st = Tbl_adv.objects.get(u=user)
                if st.Adv_approval == True:
                    print('advocate')
                    return redirect('dash')
                else:
                    return redirect('adv')


            elif Tbl_cust.objects.filter(u=user,C_status=True):
                print("login")
                return redirect('adv')




        else:
            messages.info(request,"Wrong Passwoword")
            print("not login")
            return redirect('login')
    return render(request,'login.html')

def demologout(request):
    logout(request)
    return redirect('/')
def customer_reg(request):
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
                                                username=email)
                user.save()
                customer = Tbl_cust.objects.create(u=user, C_fname=fname, C_lname=lname, C_email=email, C_gen=gend,
                                                   C_dob=dob, C_ph=mobile, C_city=city, C_state=state, C_dist=district,
                                                   C_pin=pincode, C_status=True, C_pass=password)
                customer.save()
                messages.info(request, 'ready')



    return render(request,'cust_reg.html')

@login_required(login_url='login')
def bookingfun(request,pid,bid):
    t = Tbl_adv.objects.get(id=pid)
    c = Tbl_cust.objects.get(u=request.user)
    if request.method == 'POST':
        ce=request.POST['case']
        doc=request.FILES['doc']
        cs = case(booking_id=bid,customer=c,adv=t,case_details=ce,document=doc)
        cs.save()
        return redirect('/')
    return render(request,'booking.html')


# Create your views here.
@login_required(login_url='login')
def actionbook(request,pid):
    t = Tbl_adv.objects.get(id=pid)
    print(t,'adv')
    c = Tbl_cust.objects.get(u=request.user)
    book = booking(customer=c, adv=t)
    book.save()
    print('success')
    return redirect('booking',pid=pid,bid=book.id)


@login_required(login_url='login')
def bookingview(request):
    try:
        t=Tbl_cust.objects.get(u=request.user)
        b=case.objects.filter(customer=t)
    except:
        b=''
        pass
    return render(request,'mybook.html',{'bv':b})


def cardynamic(request):
    card = request.GET.get('card')
    card_details = Customer_card_details_class.objects.get(id=card)
    return render(request,'modules.html',{'cd':card_details})


def payment(request,bid,amt):
    cards = Customer_card_details_class.objects.filter(customer__u=request.user)
    try:
        cd = Customer_card_details_class.objects.filter(customer__u=request.user).order_by('-id').first()
    except:
        cd=''
    if request.method == 'POST':
        cno = request.POST['cno']
        exp = request.POST['exp']
        cv = request.POST['cvv']
        pn = request.POST['pin']
        cname = request.POST['cname']
        if Customer_card_details_class.objects.filter(customer__u=request.user,card_no=cno).exists():
            return redirect('pcfm',bid,amt)
        else:
            cd = Customer_card_details_class(customer=Tbl_cust.objects.get(u=request.user),card_no=cno,expiry_date=exp,cvv=cv,pin=pn,card_holder_name=cname)
            cd.save()
            return redirect('pcfm',bid,amt)
    return render(request,'payment.html',{'cd':cd,'cards':cards})

# Payment Confirmation
@login_required(login_url='login')
def Payment_confirmation(request,bid,amt):
    book = case.objects.get(id=bid)
    random_number = ''.join([str(random.randint(0, 9)) for i in range(16)])
    if request.method == 'POST':
        p = Payment_Confirmation(book_id=book.booking.id,amount=amt,transaction=random_number)
        p.save()
        bk = booking.objects.get(id=book.booking.id)
        bk.paid='paid'
        bk.save()
        return redirect('bview')
    return render(request,'pcfm.html',{'cs':book,'amt':amt})


def adv_list(request,id):

    try:
        adv = Tbl_adv.objects.filter(Adv_subcategory=id)
    except:
        adv=-''
    return render(request,'Advlist.html',{'adv':adv})



def generate_pdf(request,id):
    # Get data for your template, you can replace it with your own dynamic data retrieval logic

    pay = Payment_Confirmation.objects.get(book_id=id)
    cs = case.objects.get(booking_id=id)
    context = {
        'trid': pay.transaction,
        'cname': pay.book.customer.C_fname,
        'aname':pay.book.adv.Adv_fname,
        'tot':pay.amount,
        'case':cs.case_details,
        'date':pay.date,
    }

    # Render the template
    template = get_template('invoice_template.html')
    html_content = template.render(context)

    # Create a PDF file
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename="your_pdf_filename.pdf"'
        return response

    return HttpResponse('Error generating PDF: %s' % pdf.err)