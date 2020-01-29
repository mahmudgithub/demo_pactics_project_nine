from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    slug = models.SlugField(max_length=48)
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=False)
    #tags = models.ManyToManyField(ProductTag, blank=True)

def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product-images")

def __str__(self):
        return self.image

class ProductTag(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return(self.slug,)



#class ProductImage(models.Model):
 #   thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)