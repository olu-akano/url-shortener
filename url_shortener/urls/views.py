from django.shortcuts import render
import random
from django.http import HttpResponse
import string
from .models import Urls
from .forms import NewUrlForm

def home(request):
    return render(request, 'index.html')

def newurl(length):
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))

def create_url(request):
    if request.method == 'POST':
        url = NewUrlForm(request.POST)
        if form.is_valid():
            new_url = url.save()
            short_url = newurl(5)
            form = NewUrlForm()
            data = {
                'form': form,
                'shortened_url': f'http://127.0.0.1:8000/{short_url}'
            }
            return render(request, 'index.html', data)
    else:
        form = NewUrlForm()
        data = {
            'form': form,
            'shortened_url': ''
        }
        return render(request, 'index.html', data)


