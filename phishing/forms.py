from django import forms
from .models import ExternalData


class ExternalDataForm(forms.ModelForm):
    
    class Meta:
        model = ExternalData 
        fields = ['url_externa']
