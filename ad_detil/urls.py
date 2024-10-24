"""
URL configuration for advocate_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import path

from . import views

urlpatterns = [
    path('dash/', views.admindash,name='dash'),
    path('staffreg/', views.staffreg,name='staffreg'),
    path('category/', views.category,name='category'),
    path('subcat/', views.subcat,name='subcat'),
    path('catetbl/', views.catetbl,name='catetbl'),
    path('subtbl/', views.subtbl,name='subtbl'),
    path('stafftbl/', views.stafftbl,name='stafftbl'),
    path('advtbl/', views.advtbl,name='advtbl'),
    path('custtbl/', views.custtbl,name='custtbl'),
    path('bk/', views.bk,name='bk'),
    path('edit/<int:pid>/', views.edit, name='update'),
    path('activatebtn/<int:pid>/', views.activate, name='activatebtn'),
    path('deactivatebtn/<int:pid>/', views.deactivate, name='deactivatebtn'),
    path('subedit/<int:pid>/', views.subedit, name='subupdate'),
    path('database-to-excel/', views.database_to_excel_booking, name='dexbook'),
    path('database-to-excel_customer/', views.database_to_excel_customer, name='dexcustomer'),
    path('database-to-excel_staff/', views.database_to_excel__staff, name='dexstaff'),
    path('database-to-excel_adv/', views.database_to_excel_advocate, name='dexadv'),
    path('advactivatebtn/<int:pid>/', views.advactivate, name='advactivatebtn'),
    path('advdeactivatebtn/<int:pid>/', views.advdeactivate, name='advdeactivatebtn'),
    path('custactivatebtn/<int:pid>/', views.custactivate, name='custactivatebtn'),
    path('custdeactivatebtn/<int:pid>/', views.custdeactivate, name='custdeactivatebtn'),
    path('logout', views.demologout, name='logout'),
    path('paytbl',views.paytbl, name='paytbl'),
    path('booktbl',views.booktbl, name='booktbl'),
    path('adv_view',views.adv_view,name='adview'),
    path('advapproval/<int:id>/',views.adv_approval,name='adva'),
    path('advdeapproval/<int:id>/', views.adv_deapproval, name='advd'),
    #path('pdffile',views.generate_pdf,name='pdffile'),
    path('adbook',views.adbooktbl,name='adb'),
    path('adpay', views.adpaytbl, name='adp'),
    path('stffpdv',views.staffpdf,name='stfpdf')


]
