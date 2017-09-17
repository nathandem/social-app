"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from accounts import - actually not
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name="home"),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^accounts/', include('accounts.urls',namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # strange that we include 2 urls.py for a single app!
    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^groups/',include("groups.urls", namespace="groups")),
]
# seems like there's a seperation of scope btw accounts and the project:
# - accounts app takes care of user creation (quite small scope)
# - the project takes care of login/logout (as long as base and home - normal)
# Wouldn't it be more efficient that accounts handle login/logout as well?
