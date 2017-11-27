#from django.shortcuts import render

# Create your views here.

#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response

from carrinho.models import ItemCarrinho, Carrinho
from carrinho.serializers import ItemCarrinhoSerializer, CarrinhoSerializer, UserSerializer
#from django.db.models import Sum
#from produtos.models import Produto

from django.contrib.auth.models import User
from rest_framework import permissions
from carrinho.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets


class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ItemCarrinho , acoes - list, create, retrieve, update, and detroy.
    """ 
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class CarrinhoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ItemCarrinho , acoes - list, create, retrieve, update, and detroy.
    """
    queryset = Carrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
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
#def carrinho_list(request, format=None):
#        """
#        Lista todos os carrinhos ou cria um novo carrinho
#        """
#
#        if request.method == 'GET':
#            carrinhos = Carrinho.objects.all()
#           #soma = Produto.objects.aggregate(soma_itens=Sum('valor'))
#            soma = (Produto.objects.aggregate(total=Sum('valor'))['total'])
#            Carrinho.subtotal = soma
#            serializer = CarrinhoSerializer(carrinhos, many=True)
#            return Response(serializer.data)
#        elif request.method == 'POST':
#            serializer = CarrinhoSerializer(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data, status=status.HTTP_201_CREATED)
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#@api_view(['GET', 'POST','DELETE'])
#def item_carrinho_list(request, pk , format=None):
#    """
#    Listar, Adicionar, Remover Items do Carrinho
#    """
#    try:
#        carrinho = Carrinho.objects.get(pk=pk)
#    except Carrinho.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'POST':
#        serializer = ItemCarrinhoSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    elif request.method == 'GET':
#        items_carrinho = ItemCarrinho.objects.all()
#        soma = ( ItemCarrinho.objects.aggregate(total=Sum('valor'))['total'])
#        ItemCarrinho.valor = soma
#        serializer = ItemCarrinhoSerializer(items_carrinho, many=True)
#        return Response(serializer.data)
#    elif request.method == 'DELETE':
##        try:
#        item_carrinho = ItemCarrinho.object.get(pk=pk)
##        except:
##            return Response(status=status.HTTP_404_NOT_FOUND)
#        item_carrinho.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
