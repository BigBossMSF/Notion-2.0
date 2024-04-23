from . import views
from django.urls import path

urlpatterns = [
    path('', views.note_list, name="home"),
    path('about/', views.about, name="about"),
    path('add/', views.add_note, name='add_note'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/delete/<int:note_id>/', views.delete_note, name='delete_note')
]
