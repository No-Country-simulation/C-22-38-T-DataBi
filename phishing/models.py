from django.db import models

class ExternalData(models.Model):
    url_externa=models.URLField()
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.url_externa
