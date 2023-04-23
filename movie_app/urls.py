from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.all_directors),
    path('directors/<int:id_director>', views.one_director, name='movie-director'),
    path('actors/', views.all_actors),
    path('actors/<int:id_actor>', views.one_actor, name='movie-actor'),
]