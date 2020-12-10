from django.shortcuts import render
from product.models import Product , Category
# Create your views here.

def home(request):
    
    all_category = Category.objects.all() 
    productlist = Product.objects.all()

    template = 'home/home.html'
    context = { 'all_category' : all_category , 'product_list' : productlist}

    return render(request , template , context)

# def productdetail(request, product_slug):
#     print(product_slug)
#     productdetail = Product.objects.get(slug=product_slug)
#     productimages = ProductImage.objects.filter(Product=productdetail)
#     template = 'home/product_detail.html' 
#     context = {'product_detail':productdetail, 'product_images':productimages}

#     return render(request, template, context)