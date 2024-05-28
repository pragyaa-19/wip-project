from django.shortcuts import render,  HttpResponse
from  datetime import  datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {

        "variable1":"i am pragya",
        "variable2":"this is sent"

    }
    messages.success(request,"this is icecream site")
    return render( request, 'index.html', context)

    #return HttpResponse("Hii this is a homepage")

def about(request):
    return render( request, 'about.html')
    #return HttpResponse("Hii this is a about")

def services(request):
     return render( request, 'services.html')
    #return HttpResponse("Hii this is a services page")

def contact(request):
     if request.method == "POST":

        name  = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc =  request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()

        messages.success(request, "Your data has been sent!")

     return render( request, 'contact.html')
    #return HttpResponse("Hii this is a contact page")
  
  