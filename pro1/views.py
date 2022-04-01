
# Create your views here.
from  django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params={ 'name':'harry','place':'mars'}
    return  render(request,'index.html',params)



def  analyze(request):

    print(request.GET.get('text','default'))
    print(request.GET.get('removepunc','default'))

    return  render(request,'analyzed.html')



def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def services(request):
    return render(request,'services.html')




        

# def  capitalizefirst(request):
#     return  HttpResponse("cap")
#
#
# def newlineremove(request):
#     return  HttpResponse("newline")
#
#
# def spaceremove(request):
#     return  HttpResponse("spaceremove")
#
# def charcount(request):
#     return  HttpResponse("charcount")
