from IPython.utils.contexts import preserve_keys
from django.shortcuts import render, get_list_or_404, redirect
from .models import News
from main.models import Main


# Create your views here.

def news_detail(request, word):
    site = Main.objects.get(pk=2)
    news = News.objects.filter(name=word)
    return render(request, 'front/news_detail.html', {'news': news})


def news_list(request):
    news = News.objects.all()
    return render(request, 'back/news_list.html', {'news': news})
