from IPython.utils.contexts import preserve_keys
from django.shortcuts import render, get_list_or_404, redirect
from .models import News
from main.models import Main
from cat.models import Cat
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
    cat = Cat.objects.all()
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        category = request.POST.get('newscat')
        shorttext = request.POST.get('newstxtshort')
        bodytxt = request.POST.get('newstxt')

        if newstitle == "" or shorttext == "" or bodytxt == "" or category == "":
            error = "All fields required"
            return render(request, 'back/error.html', {'error': error})

        try:

            fs = FileSystemStorage()
            myfile = request.FILES['myfile']
            filename = fs.save(myfile.name, myfile)
            media_url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:
                    b = News(name=newstitle, headline=shorttext, body_text=bodytxt, picname=filename, picurl=media_url,
                             writer='vineet', catname=category,
                             catid=0, show=0)
                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "file too large, Upload supported then 5Mb"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "file not supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            error = "Select image to upload"
            return render(request, 'back/error.html', {'error': error})
    return render(request, 'back/news_add.html', {'cat': cat})


def news_delete(request, pk):
    try:
        b = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(b.picname)
        b.delete()
    except:
        error = "failed to delete news"
        return render(request, 'back/error.html', {'error': error})
    return redirect('news_list')
