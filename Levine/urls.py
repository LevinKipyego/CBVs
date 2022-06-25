
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path(r'admin/',admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    path(r'articles/',include("myapp.urls")),   
    path(r'about/',views.about),
    path(r'',views.homepage),
]
