from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the Movies API",
        "version": "v1",
        "endpoints": {
            "movies": "/api/v1/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
]
