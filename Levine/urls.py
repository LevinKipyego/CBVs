
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path(r'zuri-admin/',admin.site.urls),
    path(r'articles/',include("myapp.urls")),
    path(r'about/',views.about),
    path(r'',views.homepage),
]
