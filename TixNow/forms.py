from django import forms
import datetime
from .models import TixGet

class getEvents(forms.Form):
    genre = forms.CharField()
    start = forms.DateField()
    end = forms.DateField()
    zipcode = forms.CharField()

    def clean(self):
        cleaned_data = super(getEvents, self).clean()
        genre = cleaned_data.get('genre')
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')
        zipcode = cleaned_data.get('zipcode')
        if not genre or not start or not zipcode:
            raise forms.ValidationError('You have to write something!')
        
        

        