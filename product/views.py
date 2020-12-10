from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, ProductImage, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here. 
def productlist(request, category_slug=None):
    category = None
    productlist = Product.objects.all().order_by('-created')
    categorylist = Category.objects.annotate(total_products=Count('product'))
    

    if category_slug :
        category = Category.objects.get(slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('q')
    if search_query :
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query)
        )

    paginator = Paginator(productlist, 20) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)
    template = 'product/product_list.html'
    context = {'product_list':productlist, 'category_list':categorylist, 'category':category}

    

    return render(request, template, context)
    

def productdetail(request, product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImage.objects.filter(Product=productdetail)
    template = 'product/product_detail.html' 
    context = {'product_detail':productdetail, 'product_images':productimages}

    return render(request, template, context)