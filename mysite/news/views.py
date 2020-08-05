from IPython.utils.contexts import preserve_keys
from django.shortcuts import render, get_list_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage


# Create your views here.

def news_detail(request, word):
    site = Main.objects.get(pk=2)
    news = News.objects.filter(name=word)
    return render(request, 'front/news_detail.html', {'news': news})


def news_list(request):
    news = News.objects.all()
    return render(request, 'back/news_list.html', {'news': news})


def add_news(request):
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        category = request.POST.get('newscat')
        shorttext = request.POST.get('newstxtshort')
        bodytxt = request.POST.get('newstxt')

        if newstitle == "" or shorttext == "" or bodytxt == "" or category == "":
            error = "All fields required"
            return render(request, 'back/error.html', {'error': error})

        fs = FileSystemStorage()
        myfile = request.FILES['myfile']
        filename = fs.save(myfile, myfile)
        media_url = fs.url(filename)
        b = News(name=newstitle, headline=shorttext, body_text=bodytxt, pic=media_url, writer='vineet', catname=category,
                 catid=0, show=0)
        b.save()
        return redirect('news_list')
    return render(request, 'back/news_add.html')
