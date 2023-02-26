from django.urls import path
from django.http import HttpResponse
from recipes.views import home
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
