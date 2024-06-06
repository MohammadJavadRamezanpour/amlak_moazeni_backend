from django.db import models

# Create your models here.
class Settings(models.Model):
    phone = models.CharField(max_length=15)
    address = models.TextField()

class Menues(models.Model):
    parent = models.ForeignKey("settings.Menues", on_delete=models.CASCADE, null=True, blank=True)
    icon = models.CharField(max_length=250)
    text = models.CharField(max_length=100)
    link = models.TextField()
    active = models.BooleanField(default=True)

    def sub_menues(self):
        return Menues.objects.filter(parent=self, active=True)