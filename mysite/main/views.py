from django.shortcuts import render, get_list_or_404, redirect
from .models import Main


# Create your views here.

def home(request):
    return render(request, 'home.html')
