from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):

    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used"),
    )

    ADS_LOCATION = (
        ("Kumasi", "Kumasi"),
        ("Accra", "Accra"),
        ("Takoradi", "Takoradi"),
    )

    NEGOTIABILITY = (
        ("Yes", "Yes"),
        ("No", "No"),
    )



    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, default = None, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    location = models.CharField(max_length=100, choices=ADS_LOCATION)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    negotiable = models.CharField(max_length=100, choices=NEGOTIABILITY)
    image = models.ImageField(upload_to='main_products/', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    


    def save(self, *args, **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    def __str__(self):
        return self.Product.name



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    fa_class = models.CharField(max_length=15)
    image = models.ImageField(upload_to='Category/', blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name :
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name



class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand_name