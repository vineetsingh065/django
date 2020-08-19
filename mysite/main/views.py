from django.shortcuts import render, get_list_or_404, redirect
from .models import Main
from .query_set.basic_render_query import render_header_footer
from news.models import News
from cat.models import Cat
from subcat.models import SubCat


# Create your views here.

def home(request):
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    return render(request, 'front/home.html', {'site': render_header_footer(), 'news': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews})


def about(request):
    return render(request, 'front/about.html', {'site': render_header_footer()})


def panel(request):
    return render(request, 'back/home.html')


def my_login(request):

    return render(request, 'front/login.html')
