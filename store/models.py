import magic
from django.db import models

class File(models.Model):
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="files", null=True, blank=True)
    extension = models.CharField(max_length=100, null=True, blank=True)
    mimetype = models.CharField(max_length=100, null=True, blank=True)

    @staticmethod
    def get_extension(file_name):
        return file_name.split(".")[-1]
    
    @staticmethod
    def get_mimetype(file_path):
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)

    def save(self, *args, **kwargs):
        # Save the file first to ensure it has a valid path
        super().save(*args, **kwargs)
        
        # Update extension and mimetype after the initial save
        self.extension = File.get_extension(self.file.name)
        self.mimetype = File.get_mimetype(self.file.path)
        
        # Save the updated model instance with new extension and mimetype
        super().save(update_fields=['extension', 'mimetype'])

    def __str__(self):
        return self.file.name
    
class Category(models.Model):
    image = models.ImageField(upload_to="files", null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    @property
    def count(self):
        self.products.filter(active=True).count()
    

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

    