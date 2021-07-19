from django.shortcuts import render
from .models import bookProduct
# Create your views here.

def home(request):
    product_list = bookProduct.objects.all()
    context = {product_list: 'product_list'}
    return render(request, 'base.html', context)