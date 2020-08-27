from django.shortcuts import render, get_list_or_404, redirect
from .models import Main
from .query_set.basic_render_query import render_header_footer
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


# Create your views here.

def home(request):
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    return render(request, 'front/home.html', {'site': render_header_footer(), 'news': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews})


def about(request):
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    return render(request, 'front/about.html', {'site': render_header_footer(), 'news': news, 'cat': cat, 'subcat': subcat})


def panel(request):
    # login check
    if not request.user.is_authenticated:
        return redirect('my_login')

    return render(request, 'back/home.html')


def my_login(request):
    if request.method == 'POST':
        uuser = request.POST.get('username')
        upass = request.POST.get('password')
        if uuser != "" or upass != "":
            user = authenticate(username=uuser, password=upass)
            if user != None:
                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def my_logout(request):

    logout(request)
    return redirect('my_login')


def site_settings(request):
    # login check
    if not request.user.is_authenticated:
        return redirect('my_login')

    if request.method == 'POST':
        site_name = request.POST.get('name')
        contact = request.POST.get('contact')
        facebook = request.POST.get('fb')
        twitter = request.POST.get('tw')
        youtube = request.POST.get('yt')
        about = request.POST.get('about')

        if facebook == "" : facebook = '#'
        if twitter == "" : twitter = '#'
        if youtube == "" : youtube = '#'

        if site_name=="" or about == "":
            error = "All fields required"
            return render(request, 'back/error.html', {'error': error})

        try:

            fs = FileSystemStorage()
            myfile = request.FILES['myfile']
            filename = fs.save(myfile.name, myfile)
            media_url = fs.url(filename)

            b = Main.objects.get(pk=2)
            b.name = site_name
            b.contact = contact
            b.fb = facebook
            b.tw = twitter
            b.yt = youtube
            b.about = about
            b.logo_name = filename
            b.logo_url = media_url
            b.save()

        except:
            b = Main.objects.get(pk=2)
            b.name = site_name
            b.contact = contact
            b.fb = facebook
            b.tw = twitter
            b.yt = youtube
            b.about = about
            b.save()

    site = Main.objects.get(pk=2)

    return render(request, 'back/settings.html', {'site': site})


def contact(request):
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()


    return render(request, 'front/contact.html', {'site': render_header_footer(), 'news': news, 'cat': cat,
                                                  'subcat': subcat})

