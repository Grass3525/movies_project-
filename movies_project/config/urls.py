from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token



def home(request):
    return JsonResponse({
        "message": "Welcome to the Movies API",
        "version": "v1",
        "endpoints": {
            "movies": "/api/v1/movies/",
            "streaming_channels": "/api/v1/channels/",
            "admin": "/admin/"
        }
    })


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/auth/token/', obtain_auth_token),

]
