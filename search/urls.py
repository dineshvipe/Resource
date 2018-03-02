
from django.conf.urls import url , include
from django.contrib import admin
from . import views

app_name='search'

urlpatterns = [
    url(r'^search/',views.search,name='search1'),
    url(r'^Warning/',views.returnWarningPage,name='warningPages'),
]
