from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def register_page(request):
    return render(request, 'frontend/register.html')
