from django.contrib import admin
from django.urls import path, include
from .viwes import landig

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landig),
    path("", include("Library.urls")),
    path("", include("Users.urls")),
]
