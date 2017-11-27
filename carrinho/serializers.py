from rest_framework import serializers
from carrinho.models import ItemCarrinho, Carrinho
from produtos.models import Produto
from django.contrib.auth.models import User

class ItemCarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(many=True, view_name='produto-detail', read_only=True)
    class Meta:
        model = ItemCarrinho
        fields = ( 'url' , 'item' , 'quantidade' )

class CarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(many=True, view_name='itemcarrinho-detail', read_only=True)
    class Meta:
        model = Carrinho
        fields = ( 'url', 'id', 'items', 'subtotal')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    carrinho = serializers.HyperlinkedRelatedField(many=True, view_name='carrinho-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'carrinho')
