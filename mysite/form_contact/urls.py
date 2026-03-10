from django.urls import path

from . import views

urlpatterns = [
    path('submit/', views.submit, name='form_contact_submit'),
]
