from django.contrib import admin
from django.urls import path
from .views import UsuarioRecebidoApiView

urlpatterns = [
    path('usuarios/', UsuarioRecebidoApiView.as_view(), name='usuario_recebido_api_view'),
    path('usuarios/<int:pk>/', UsuarioRecebidoApiView.as_view(), name='usuario_recebido_api_view_pk'),
]
