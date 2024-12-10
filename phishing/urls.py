from django.urls import path 
from .views import (phishing_view,home_view)


urlpatterns = [
    path('',home_view,name='home'),
    path('phishingurl/',phishing_view,name='phishingurl')
]
