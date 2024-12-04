from django.urls import path 
from .views import (phishing_view)


urlpatterns = [
    path('phishingurl/',phishing_view,name='phishingurl')
]
