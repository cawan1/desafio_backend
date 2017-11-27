from produtos.models import Produto, Carrinho, ItemCarrinho
from produtos.serializers import ProdutoSerializer, UserSerializer, CarrinhoSerializer, ItemCarrinhoSerializer

from django.contrib.auth.models import User
from rest_framework import permissions
from produtos.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets


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

class CarrinhoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o Carrinho
    """
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ItemCarrinho
    """
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
