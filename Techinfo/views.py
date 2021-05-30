from django.shortcuts import render, HttpResponse
from datetime import datetime
from Techinfo.models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')