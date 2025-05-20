"""
URL configuration for Blog_here project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('register/',register_view,name="register"),
    path('login/',login_view,name="login"),
    path('add_post/',add_post_view,name="add_post"),
    path('update_profile/',update_profile_view,name="update_profile"),
    path('update_post/<int:id>',update_post_view,name="update_post"),
    path('show_profile/',show_profile_view,name="show_profile"),
    path('other_profile/<id>',other_profile_view,name="other_profile"),
    path('logout/',logout_view,name="logout"),
    path('admin_panel',admin_panel_view),
    path('search/',search_view,name="search"),
    path('post_detail/<id>',post_detail_view,name="post_detail"),
    path('delete_post/',delete_post_view,name="delete_post"),
    
  



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
