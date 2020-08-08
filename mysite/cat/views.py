from django.shortcuts import render, get_list_or_404, redirect
from .models import Cat


# Create your views here.

def cat_list(request):
    cat = Cat.objects.all()
    return render(request, 'back/cat_list.html', {'cat': cat})


def add_cat(request):
    if request.method == "POST":
        category_name = request.POST.get('catname')
        if category_name == "":
            error = "Enter Category name"
            return render(request, 'back/error.html', {'error': error})
        if len(Cat.objects.filter(name=category_name)) != 0:
            error = "Category already exist"
            return render(request, 'back/error.html', {'error': error})
        b = Cat(name=category_name)
        b.save()
    return render(request, 'back/cat_add.html')
