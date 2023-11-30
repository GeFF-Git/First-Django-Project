from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def home(request):
    a = 5|3
    if(a==7):
        return render(request,'index.html',{'name':'GeFF!!','price':999})

    else:
        return render(request,'home.html',{'name':'Shelby!!'})

def add(request):
    n1 =int( request.POST['num1'])
    n2 =int( request.POST['num2'])
    result = n1+n2
    return render(request,'result.html',{"result":result})    

def index(request):
    dests = Destination.objects.all()
    return render(request,"index.html",{'dests' : dests})

    
    
#  dest1 = Destination()
#     dest1.name = 'Chennai'
#     dest1.desc = 'The city which unites diverse people'
#     dest1.price = 999
#     dest1.img = 'destination_1.jpg'
#     dest1.offer = True

#     dest2 = Destination()
#     dest2.name = 'Tirunelveli'
#     dest2.desc = 'Oxford of Tamilnadu'
#     dest2.price = 999
#     dest2.img = 'destination_2.jpg'
#     dest2.offer = False

#     dest3 = Destination()
#     dest3.name = 'Tuticorin'
#     dest3.desc = 'Pearl city'
#     dest3.price = 999
#     dest3.img = 'destination_4.jpg'
#     dest3.offer = False

#     dests = [dest1,dest2,dest3]    