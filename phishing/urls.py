from django.urls import path 
from .views import (phishing_view,home_view,external_data_view,features_view)


urlpatterns = [
    path('',home_view,name='home'),
    path('phishingurl/',phishing_view,name='phishingurl'),
    path('predict/',external_data_view,name='phishing'),
    path('dashboard/',features_view,name='dashboard'),
    #path('mostrarcsv/',mostrar_csv_view, name='mostrarcsv'),
]
