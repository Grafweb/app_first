from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('contact', views.contact, name='contact'),
    path('contact-form', views.contact_form, name='contact-form'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery-thumbs', views.gallery_thumbs, name='gallery-thumbs'),
    path('menu', views.menu, name='menu'),
    path('mobile-menu', views.mobile_menu, name='mobile-menu'),
]