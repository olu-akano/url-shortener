from django.shortcuts import render
import random
from django.http import HttpResponse
import string

def home(request):
    return render(request, 'home.html')

def show_url(request):
    return render(request, 'showurl.html')

def newurl(length):
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))

def create_url(request):
    if request.method == 'POST':
        form = NewUrlForm(request.POST)
        if form.is_valid():
            short_url = newurl(5)
            # new_url = request.POST['new_url']
            new_url = Urls(url='test', short_url='short_url')
            url.save()
            return redirect("new-url", result=url)
    else:
        form = NewUrlForm()
        data = Urls.objects.all()
        context = {
            'form': form,
            'data': data
        }
        return render(request, 'home.html', context)


