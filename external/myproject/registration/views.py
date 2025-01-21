from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register_page(request):
    if(request.method=="GET"):
        return render(request, 'folder/register.html')


def handle_submit(request):
    if(request.method=="POST"):
        name= request.POST.get('name')
        email=request.POST.get('email')
        age = request.POST.get('age')
        course = request.POST.get('course')
        return render(request, 'folder/welcome.html', {"name":name})
        
        