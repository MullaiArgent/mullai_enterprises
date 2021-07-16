from django.shortcuts import render
from .models import products

# Create your views here.
def home(request):
    product = products.objects.all()
    return render(request,'index.html',{'product' : product})

