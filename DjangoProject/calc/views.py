from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    a = 5|3
    if(a==7):
        return render(request,'home.html',{'name':'GeFF!!'})

    else:
        return render(request,'home.html',{'name':'Shelby!!'})

    

def add(request):
    n1 =int( request.POST['num1'])
    n2 =int( request.POST['num2'])
    result = n1+n2
    return render(request,'result.html',{"result":result})    