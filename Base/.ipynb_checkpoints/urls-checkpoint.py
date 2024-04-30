from django.contrib import admin
from django.urls import path,include
from Base import views

admin.site.site_header = "Personal Finance Management Admin"
admin.site.site_title = "Personal Finance Management Admin Portal"
admin.site.index_title = "Welcome to Personal Finance Management"
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact')
]