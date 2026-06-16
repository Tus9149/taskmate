from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from todolist_app import views as tdapp_views
from users_app import views as userapp_views



urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('todolist/',include('todolist_app.urls')),
    path('contact',tdapp_views.contact,name='contact'),
    path('about',tdapp_views.about,name='about'),
    path('',tdapp_views.index,name='index'),
     path('account/',include('users_app.urls')),
]