from django.shortcuts import render, get_list_or_404, redirect
from .models import SubCat
from cat.models import Cat


# Create your views here.

def subcat_list(request):
    subcat = SubCat.objects.all()
    return render(request, 'back/subcat_list.html', {'subcat': subcat})


def add_subcat(request):
    cat = Cat.objects.all()
    if request.method == "POST":
        subcategory_name = request.POST.get('subcatname')
        catid = request.POST.get('category')
        if subcategory_name == "" or cat == "":
            error = "Sub Category or Category not chosen"
            return render(request, 'back/error.html', {'error': error})
        if len(SubCat.objects.filter(name=subcategory_name)) != 0:
            error = "Category already exist"
            return render(request, 'back/error.html', {'error': error})

        catname = Cat.objects.get(pk=catid).name
        b = SubCat(name=subcategory_name, catname=catname, catid=catid)
        b.save()
        return redirect('subcat_list')

    return render(request, 'back/subcat_add.html', {'cat': cat})
