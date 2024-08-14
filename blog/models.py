from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    thumbnail = models.ImageField(upload_to="files", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title