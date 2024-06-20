from django.db import models


class Settings(models.Model):
    phone = models.CharField(max_length=15)
    address = models.TextField()
    intro_image = models.ImageField(upload_to="files", null=True, blank=True)
    intro_header = models.CharField(max_length=15, null=True, blank=True)
    intro_text = models.TextField(null=True, blank=True)


class Menues(models.Model):
    parent = models.ForeignKey(
        "settings.Menues", on_delete=models.CASCADE, null=True, blank=True
    )
    icon = models.CharField(max_length=250)
    text = models.CharField(max_length=100)
    link = models.TextField()
    active = models.BooleanField(default=True)

    @property
    def sub_menues(self):
        return Menues.objects.filter(parent=self, active=True)
    

class Slider(models.Model):
    image = models.ImageField(upload_to="files")
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
