from django.urls import path
from . import views
urlpatterns=[

    path('advocate', views.advreg, name='ajax_load_branch'),
    #path('ajax/load-cat', views.load_cat, name='ajax_load_branch'),
    path('get_subcategories', views.get_subcategories, name='get_subcategories'),
    path('advocate_registration', views.advocate_registration, name='advocate_registration'),
    path('advocate_bookings',views.booking_details,name='advb'),
    path("bookreject/<int:id>/",views.Booking_Rejection,name='rbk'),
]