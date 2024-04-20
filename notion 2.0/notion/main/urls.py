from . import views
from django.urls import path

urlpatterns = [
    path('', views.note_list, name="home"),
    path('about/', views.about, name="about"),
    path('add/', views.add_note, name='add_note')
]
