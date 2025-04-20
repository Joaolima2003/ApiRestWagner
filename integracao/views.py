from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import UsuarioRecebido
from .serializers import UsuarioRecebidoSerializer


class UsuarioRecebidoApiView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        usuarios = UsuarioRecebido.objects.all()
        serializer = UsuarioRecebidoSerializer(usuarios, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UsuarioRecebidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            usuario = UsuarioRecebido.objects.get(pk=pk)

        except UsuarioRecebido.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioRecebidoSerializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            usuario = UsuarioRecebido.objects.get(pk=pk)
        except UsuarioRecebido.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


