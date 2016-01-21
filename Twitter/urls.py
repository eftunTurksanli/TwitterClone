"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from main import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^registerForm$', views.register, name='register'),
    url('^$', views.main, name='main'),
    url('^addTweet/$', views.new_tweet, name='tweet'),
    url('^login$', views.login_page, name="login_page"),
    url('^profile/(?P<username>\w+)$', views.profile, name='profile'),
    url('^settings/$', views.settings, name='settings'),
    url('^profile_pic/$', views.profile_pic, name='profile_pic'),
    url(r'^logout/', views.log_out, name='log_out'),
    url(r'^follow/(?P<username>\w+)$', views.follow, name='follow'),
    url('^likes/(?P<username>\w+)/(?P<id>\d+)$', views.likes, name='likes'),
    url(r'^all_messages$', views.all_messages, name='all_messages'),
    url(r'^send_messages/(?P<username>\w+)$', views.send_message, name='send_message'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
