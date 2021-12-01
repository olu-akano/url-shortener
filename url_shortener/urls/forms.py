from django import forms
from .models import Urls

class NewUrlForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ['url', 'short_url']