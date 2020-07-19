from django.shortcuts import render, get_list_or_404, redirect
from .models import Main
from .query_set.basic_render_query import render_header_footer


# Create your views here.

def home(request):
    return render(request, 'front/home.html', {'site': render_header_footer()})


def about(request):
    return render(request, 'front/about.html', {'site': render_header_footer()})
