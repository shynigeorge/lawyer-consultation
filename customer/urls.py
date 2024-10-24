from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='adv'),
    path('cust_reg', views.customer_reg, name='cust_reg'),
    path('login', views.loginpage, name='login'),
    path('logout', views.demologout, name='logout'),
    path('booking/<int:pid>/<int:bid>/', views.bookingfun, name='booking'),
    path('book/<int:pid>/',views.actionbook,name='book'),
    path('bview',views.bookingview,name='bview'),
    path('payment/<int:bid>/<int:amt>/',views.payment,name='pay'),
    path('paymentconf/<int:bid>/<int:amt>/',views.Payment_confirmation,name='pcfm'),
    path('Advlist/<int:id>/',views.adv_list,name='alist'),
    path('pdf/<int:id>/',views.generate_pdf,name='pdf'),
    path('carddynamic',views.cardynamic,name='carddyn'),
    path('casesshow',views.Cases_show,name='cases_show'),

]