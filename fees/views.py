from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from  fees.models import Contact

# Create your views here.




def index(request):
    return render(request,'fees/index.html')



def Home(request):
    return HttpResponse("this is home page")


def about(request):
    return HttpResponse("this is home page")

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')

        email=request.POST.get('email')

        phone=request.POST.get('phone')

        city=request.POST.get('city')

        state=request.POST.get('state')
        contact=Contact(name=name,email=email,phone=phone,city=city,state=state,date=datetime.today())
        contact.save()
    return render(request,'fees/contact.html')
    

def services(request):
    return HttpResponse("this is home page")
    


def client(request):
    return render(request,'pro1/client.html')