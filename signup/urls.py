from django.conf.urls import url , include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name='signup'

from signup import views
urlpatterns = [
    
    #url(r'^admin/', admin.site.urls),
    #url(r'^signup/',include('signup.urls')),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='signup/login.html'), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$',views.SignUp.as_view(), name='signup'),
    url(r'^first/$',views.look,name="firstpage"),
    url(r'^verify/',views.verifyPage,name="verifyPage"),
    url(r'^verifyOtp/',views.verifyOtp,name='verifyOtp'),
    url(r'^loginUser/',views.loginUser,name="loginUser"),
    url(r'^get_drugs/', views.get_drugs, name='get_drugs'),
    url(r'^loadProfile/',views.loadUserProfile,name='loadUserProfile'),
    url(r'^profile/',views.Profile,name='profile'),
    # FOR THE USER PAGE HERE

    # /modelforms/
    #url(r'^$', views.IndexView.as_view(), name='index'),

    # modelforms/product/entry
    #url(r'^user/entry/$',views.UserEntry.as_view(),name='user-entry'),

    # modelforms/product/2
    #url(r'^user/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='user-update'),

    # modelforms/product/(?P<pk>[0-9]+)/delete
    #url(r'^user/(?P<pk>[0-9]+)/delete$', views.UserDelete.as_view(), name='user-delete'),


    #url(r'^send/',mail.send,name='send'),
    #url(r'^$',views.see,name='see'),
]