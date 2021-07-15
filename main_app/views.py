from django.shortcuts import render
from .models import products

# Create your views here.
def home(request):
    product1 = products()
    product1.name = 'yess'
    return render(request,'index.html',{'product1' : product1})

