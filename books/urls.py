from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.detail_book, name='detail_book'),  # ← Agrega esta línea
]