from django.urls import path 
from .views import (home_view,phishing_view)


urlpatterns = [
    path('',home_view,name='home'),
    path('phishingurl/',phishing_view,name='phishingurl')
]
