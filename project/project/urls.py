from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pokedex/', include('pokedex.urls')),
    path('admin/', admin.site.urls),
]