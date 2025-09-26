from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    ##th('login/', views.loga_usuario, name= 'login'),
]