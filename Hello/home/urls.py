from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Administrator LOGIN"
admin.site.site_title = "VGI Admin Portal"
admin.site.index_title = "Welcome to vikrant graoup of institutuions!"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]
    # this is called url dispaching
    