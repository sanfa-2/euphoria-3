from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Slide(models.Model):
    title = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='slides/')  
   

    def __str__(self):
        return self.title

class CategoryForMen(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    category = models.ManyToManyField('Category', related_name='mens')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Men Categories'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'    

class CategorForWomen(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    category = models.ManyToManyField('Category', related_name='womens')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Women Categories'    

class Brand(models.Model):
    image = models.ImageField(upload_to='images/') 

    def __str__(self):
        return str(self.id)      

class Limelight(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    category = models.ManyToManyField('Category', related_name='limelights')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand_name = models.CharField(max_length=255)


    def __str__(self):
        return self.title
  


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_span = models.FileField(upload_to='testimonials/', blank=True, null=True)  
    rating = models.FloatField(default=0.0)

    
    def __str__(self):
        return self.name        


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="products/")
    gallery = models.ManyToManyField('GalleryImage')  
    comments = models.DecimalField(max_digits=10, decimal_places=2)
    brand_name = models.CharField(max_length=255)


    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/') 
    description = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Gallery Image {self.id}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

