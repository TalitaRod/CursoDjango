from django.urls import path
from django.http import HttpResponse
# from recipes.views import home #pode importar as views desta forma
from recipes import views #pode importar as views dessa forma
# from . import views e como está na mesma pasta, pode importar as views desta forma também
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('recipes/<int:id>/', views.recipe), #criando urls dinâmicas
]
