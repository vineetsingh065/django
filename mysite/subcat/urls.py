from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/subcategory/list/$', views.subcat_list, name='subcat_list'),
    url(r'^panel/add/subcategory/$', views.add_subcat, name='add_subcat'),
]