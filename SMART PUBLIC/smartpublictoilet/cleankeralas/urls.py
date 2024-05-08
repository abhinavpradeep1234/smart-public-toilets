from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.signup ,name='signup'),
    path('search/',views.search ,name='search'),

    path('booking/',views.booking ,name='booking'),
    path('complaint/',views.complaint ,name='complaint'),
    path('login/',views.login ,name='login'),
    path('logout/',views.logout ,name='logout'),
    path('home/',views.home ,name='home'),
    path('payment/',views.payment,name='payment'),
    path('learn/',views.learn,name='learn'),
    path('learns/',views.learns,name='learns'),
    path('password/',views.password,name='password'),
    path('invalid/',views.invalid,name='invalid')
    
    
    
    
    
]