#from django.shortcuts import render

# Create your views here.
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from produtos.serializers import UserSerializer

#from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from produtos.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
#from rest_framework import renderers
#from rest_framework.response import Response
#from rest_framework.decorators import detail_route


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o Produto, acoes - list, create, retrieve, update, and detroy.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list and detail actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

#@api_view(['GET', 'POST'])
#def produto_list(request, format=None):
#        """
#        Lista todos os produtos ou cria um novo produto
#        """
#        
#        if request.method == 'GET':
#            produtos = Produto.objects.all()
#            serializer = ProdutoSerializer(produtos, many=True)
#            return Response(serializer.data)
#        elif request.method == 'POST':
#            serializer = ProdutoSerializer(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data, status=status.HTTP_201_CREATED)
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def produto_detail(request, pk, format=None):
#    """
#    Selecionar , editar, excluir produtos
#    """
#    try:
#        produto = Produto.objects.get(pk=pk)
#    except Produto.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = ProdutoSerializer(produto)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        serializer = ProdutoSerializer(produto, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        produto.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
