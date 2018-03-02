from django.conf.urls import url , include
from django.contrib import admin
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^login/',include('signup.urls',namespace='login')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/',include('signup.urls',namespace='signup')),
    url(r'^signup/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.Test.as_view(),name='test'),
    url(r'^thanks/$',views.Thanks.as_view(),name='thanks'),
    url(r'^first/',include('signup.urls',namespace='firstpage')),
    #url(r'^post/',include('post.urls',namespace='postView')),
    url(r'^send/',include('signup.urls',namespace='send')),
    url(r'^verify/',include('verify.urls',namespace='verify')),
    url(r'^search/',include('search.urls',namespace='search')),
    url(r'^verifyOtp/',include('signup.urls',namespace='verifyOtp')),
    url(r'^search/',include('search.urls',namespace='search1')),
    url(r'^get_drugs/',include('signup.urls',namespace='get_drugs')),
    url(r'^loadProfile/',include('signup.urls',namespace='loadUserProfile')),
    url(r'^saveData/',include('post.urls',namespace='saveData')),
    url(r'^recommendPages/',include('recommend.urls',namespace='recommendPages')),
    url(r'^Warning/',include('search.urls',namespace='warningPages')),

    url(r'^profile',include('signup.urls',namespace='profile')),
    #url(r'^signup/',include('signup.urls')),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
