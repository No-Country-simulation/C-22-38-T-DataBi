from django.db import models
from cloudinary.models import CloudinaryField


class ExternalData(models.Model):
    url_externa=models.URLField()
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.url_externa

class LibraryC(models.Model):
    title= models.CharField(max_length=100)
    description=models.CharField( max_length=250)
    image=CloudinaryField('image')
    
    def __str__(self):
        return self.title