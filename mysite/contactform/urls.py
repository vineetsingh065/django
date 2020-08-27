from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/submit/$', views.contact_add, name='contact_add'),
]