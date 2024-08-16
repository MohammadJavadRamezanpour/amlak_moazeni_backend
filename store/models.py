from django.db import models
  
class Category(models.Model):
    image = models.ImageField(upload_to="files", null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    @property
    def count(self):
        self.products.all().count()
    

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

    def __str__(self):
        return self.title
    