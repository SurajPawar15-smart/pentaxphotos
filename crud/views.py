from django.shortcuts import render
from django.http import HttpResponse
def about_us(request):
   return render(request, 'about_us.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def element(request):
    return render(request, 'element.html')
def index(request):
    return render(request, 'index.html')
def price(request):
    return render(request, 'price.html')
def project(request):
    return render(request, 'project.html')
def project_details(request):
    return render(request, 'project_details.html')
def service(request):
    return render(request, 'service.html')
def single_blog(request):
    return render(request, 'single_blog.html')


