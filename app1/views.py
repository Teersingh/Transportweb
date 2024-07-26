from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def getdata(request):

    if request.method=="POST":

        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        start_desti=request.POST.get('from')
        to_desti=request.POST.get('to')
        message=request.POST.get('message')

        # Save to the database
        contact = Contact(name=name, email=email,phone=phone,start_desti=start_desti,to_desti=to_desti, message=message)
        contact.save()

        return HttpResponse("Thank you for contacting us!")

    return render(request, 'contact.html')

def index (request):
    if request.method=="POST":

        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        start_desti=request.POST.get('from')
        to_desti=request.POST.get('to')
        message=request.POST.get('message')
        

        print(name)
        print(email)
        print(phone)
        print(start_desti)
        print(to_desti)
        print(message)
        # Save to the database
        contact = Contact(name=name, email=email,phone=phone,start_desti=start_desti,to_desti=to_desti, message=message)
        contact.save()

        return redirect("/index/")
    return render(request,'index.html')

def about(request):
    
    return render(request,"about.html")
def company(request):
    
    return render(request,"company.html")
def contact(request):
    if request.method=="POST":

        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        start_desti=request.POST.get('from')
        to_desti=request.POST.get('to')
        message=request.POST.get('message')


        # Save to the database
        contact = Contact(name=name, email=email,phone=phone,start_desti=start_desti,to_desti=to_desti, message=message)
        contact.save()

        return redirect("/contact/")
    return render(request,"contact.html")
def shop(request):
    
    return render(request,"shop.html")

def service(request):
    
    return render(request,"service.html")

def get_city(request,city):
     
    city=city.capitalize()
    
    context= {"city": city}

    return render(request,'city.html',context)