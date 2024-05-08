from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import searchtoilets,books,reports
from.forms import booksForm,complaintForm
from django.db.models import Q
from django.contrib.auth.models import User,auth
from django .contrib.auth import authenticate,login
import razorpay



# Create your views here.
def login(request):
     if request.method=="POST":
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('home')
          else:
                 return render(request,"invalid.html")
          
     return  render(request,'login.html')
    
def home(request):
     return  render(request,'home.html')

def invalid(request):
     return  render(request,'invalid.html')
    
def search(request):
     if request.method=="POST":
          search=request.POST.get('search')
          results=searchtoilets.objects.filter(Q(s_name__icontains=search))
          sasi={'result':results}
          return render (request,'search.html',sasi)
     dict_sear={'search':searchtoilets.objects.all()}
     return  render(request,'search.html',dict_sear)
 
 
    
def signup(request):
     if request.method=="POST":
          username=request.POST['username']
          email=request.POST['email']
          password=request.POST['password']
          confirmpassword=request.POST['confirm-password']
          if  User.objects.filter(username=username).exists():
               return render(request,"learn.html")
          if password!=confirmpassword:
               return render(request,'password.html')
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save()
          return redirect('login')
     return  render(request,'signup.html')


def password(request):
     return render (request,'password.html')


def learns(request):
     return render (request,'learns.html')

def learn(request):
     return render (request,'learn.html')


def logout(request):
     return  redirect('signup')
 
 
def booking(request):
    if request.method=="POST":
        form=booksForm(request.POST)
        if form.is_valid():
         form.save()
         return render(request,'confirm.html')
    form=booksForm()
    dict_form={'form':form}
    return  render(request,'booking.html',dict_form)
 
 
 
 
 
def complaint(request):
     if request.method=="POST":
          form=complaintForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'confirms.html')
          
     form=complaintForm()
     dict_form={'form':form}
     return  render(request,'complaint.html',dict_form)





def payment(request):
     if request.method=="POST":
      amount=100,
      currency='INR'
      client = razorpay.Client(auth=("rzp_test_bExXeTSGdRlunx", "IQm8XkvZmAl3F61mT7mJLbrK"))

     payment=client.order.create({'amount':'100',"currency":"INR", 'payment_capture':1})
     return HttpResponse('hhh')