
from django.conf.urls import url , include
from django.contrib import admin
from recommend import views

app_name='recommend'

urlpatterns = [
    url(r'^$',views.recommendPages,name='recommendPages'),
]
