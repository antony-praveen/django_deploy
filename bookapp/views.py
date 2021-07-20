from django.shortcuts import render
from .models import bookProduct
# Create your views here.

def home(request):

    # count the number of books have
    total_books = bookProduct.objects.count()
    product_list = bookProduct.objects.all()
    # search functions 
    item = request.GET.get('item_name')
    if item != '' and item is not None:
        product_list = product_list.filter(name__icontains=item)

    context = {'product_list':product_list,'total_books':total_books}
    return render(request, 'base.html', context,)