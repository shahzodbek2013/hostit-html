from django.shortcuts import render


def home_page (request):
    return render(request,'index.html')

def about_page (request):
    return render(request,'about.html')

def contact_page (request):
    return render(request,'contact.html')

def price_page (request):
    return render(request,'price.html')

def service_page (request):
    return render(request,'service.html')