from . import views
from django.urls import path, include
from .views import ListActorDirector, ActorView, DirectorView

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.all_directors),
    path('directors/<int:pk>', DirectorView.as_view(), name='movie-director'),
    path('actors/', views.all_actors),
    path('actors/<int:pk>', ActorView.as_view(), name='movie-actor'),
    path('actorsdirectors', ListActorDirector.as_view()),

]
