import magic

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class File(models.Model):
    file = models.FileField(upload_to='files')
    extension = models.CharField(max_length=100, null=True, blank=True)
    mimetype = models.CharField(max_length=100, null=True, blank=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

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
  