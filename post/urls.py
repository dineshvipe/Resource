from django.conf.urls import url
from . import views
app_name='post'
urlpatterns=[
    url(r'^saveData/',views.saveUploadFormData.saveUploadFormData,name='saveData'),
]