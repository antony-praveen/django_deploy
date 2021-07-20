from django.shortcuts import render
from .models import bookProduct
from django.core.paginator import Paginator
# Create your views here.

def home(request):

    # count the number of books have
    total_books = bookProduct.objects.count()
    product_list = bookProduct.objects.all().order_by('price')
    # search functions 
    item = request.GET.get('item_name')
    if item != '' and item is not None:
        product_list = product_list.filter(bookName__icontains=item)

    paginator = Paginator(product_list,6)
    page_number = request.GET.get('mypage')#my page is just positional argument so don't care about that anything you give you want
    product_list = paginator.get_page(page_number)

    context = {'product_list':product_list,'total_books':total_books}
    return render(request, 'base.html', context,)

def author_detail(request,author_name):
    product_list = bookProduct.objects.get(id=author_name)
    # author_details = bookProduct.objects.all()
    # author_name_crop = author_details.filter(author = )
    return render(request,'author.html',{'product_list':product_list})

