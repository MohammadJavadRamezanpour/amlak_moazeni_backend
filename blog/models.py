from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    image = models.ImageField(upload_to="files", null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    @property
    def count(self):
        self.posts.filter(publish=True).count()

    def __str__(self):
        return str(self.title)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    title = models.CharField(max_length=250)
    desc = models.TextField()
    text = RichTextField()
    thumbnail = models.ImageField(upload_to="files", null=True, blank=True)
    tags = models.ManyToManyField("core.Tag")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title