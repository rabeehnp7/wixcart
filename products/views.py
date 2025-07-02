from django.shortcuts import render,get_object_or_404
from . models import Product
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.management import call_command

def run_migrate(request):
    call_command('migrate')
    return HttpResponse("Migration complete.")

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',page)
    product_list=Product.objects.all()
    paginator=Paginator(product_list,2)
    product_list=paginator.get_page(page)
    context={'products':product_list}
    return render(request,'product_list.html',context)

def product_detail(request,pro_id):
    product=get_object_or_404(Product,id=pro_id)
    return render(request,'product_detail.html',{'product':product})