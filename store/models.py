from django.db import models
  
class Category(models.Model):
    image = models.ImageField(upload_to="files", null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    @property
    def count(self):
        self.products.all().count()
    
    def __str__(self):
        return self.title
    
class Property(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ProductProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.product.title} | {self.property.title} | {self.value}"
    
class Product(models.Model):
    STATUS_CHOICES = [
        ("available", "موجود"),
        ("not available", "ناموجود"),
    ]
    price = models.IntegerField(default=0)
    rental_price = models.IntegerField(default=0)
    title = models.CharField(max_length=500)
    text = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    thumbnail = models.ImageField(upload_to="files", null=True, blank=True)
    tags = models.ManyToManyField("core.Tag")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    lat = models.CharField(max_length=500, null=True, blank=True)
    lang = models.CharField(max_length=500, null=True, blank=True)
    properties = models.ManyToManyField(Property, through=ProductProperty)

    def __str__(self):
        return self.title