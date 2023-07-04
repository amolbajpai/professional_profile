from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    names = ['Ram','Shyam']
    context = {'names': names}
    return render(request, 'home.html', context)
