
from django.urls import path
from .views import ListMovie, DetailMovie

app_name = 'movies'

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view(), name='movie-detail'),
    path('', ListMovie.as_view(), name='movie-list'),
]
