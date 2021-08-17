"""Blogchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, register, login_user, get_homepage, logout_user

urlpatterns = [
                  path('', get_homepage, name="homepage"),
                  path('home/', home, name="Home"),
                  path('Blog/<slug:url>', post),
                  path('category/<slug:url>',category),
                  path('register',register, name = "register"),
                  path('login',login_user, name = "login"),
                  path('logout', logout_user , name="logout")

    ]