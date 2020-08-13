from IPython.utils.contexts import preserve_keys
from django.shortcuts import render, get_list_or_404, redirect
from .models import News
from main.models import Main
from cat.models import Cat
from django.core.files.storage import FileSystemStorage
from subcat.models import SubCat


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
    subcat = SubCat.objects.all()
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        category = request.POST.get('newscat')
        shorttext = request.POST.get('newstxtshort')
        bodytxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')

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

                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid = SubCat.objects.get(pk=newsid).catid
                    b = News(name=newstitle, headline=shorttext, body_text=bodytxt, picname=filename, picurl=media_url,
                             writer='vineet', catname=newsname,
                             catid=newsid, show=0, ocatid=ocatid)
                    b.save()

                    count = len(News.objects.filter(ocatid=ocatid))
                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
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
    return render(request, 'back/news_add.html', {'subcat': subcat})


def news_delete(request, pk):

    try:

        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = News.objects.get(pk=pk).ocatid

        b.delete()

        count = len(News.objects.filter(ocatid=ocatid))

        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()


    except:

        error = "Somthing Wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')



def news_edit(request, pk):
    if len(News.objects.filter(pk=pk)) == 0:
        error = "News Not found"
        return render(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        category = request.POST.get('newscat')
        shorttext = request.POST.get('newstxtshort')
        bodytxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')

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

                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News.objects.get(pk=pk)
                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.headline = shorttext
                    b.body_text = bodytxt
                    b.picname = filename
                    b.picurl = media_url
                    b.catname = newsname
                    b.catid = newsid
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
            newsname = SubCat.objects.get(pk=newsid).name

            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.headline = shorttext
            b.body_text = bodytxt
            b.catname = newsname
            b.catid = newsid
            b.save()
            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cat': cat})
