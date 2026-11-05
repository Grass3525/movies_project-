
from django.urls import path
from .views import (
    ListMovie,
    DetailMovie,
    CreateMovie,
    UpdateMovie,
    DeleteMovie,
)

app_name = 'movies'

urlpatterns = [
    path('', ListMovie.as_view(), name='movie-list'),
    path('create/', CreateMovie.as_view(), name='movie-create'),
    path('<int:pk>/', DetailMovie.as_view(), name='movie-detail'),
    path('<int:pk>/update/', UpdateMovie.as_view(), name='movie-update'),
    path('<int:pk>/delete/', DeleteMovie.as_view(), name='movie-delete'),
]
