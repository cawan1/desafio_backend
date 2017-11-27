from rest_framework import serializers
from carrinho.models import ItemCarrinho, Carrinho
from produtos.models import Produto
from django.contrib.auth.models import User

class ItemCarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username', read_only=True )
    item = serializers.HyperlinkedRelatedField(many=True, view_name='produto-detail', read_only=True)
    carrinho = serializers.HyperlinkedRelatedField(many=True, view_name='carrinho-detail', read_only=True)
    class Meta:
        model = ItemCarrinho
        fields = ( 'url', 'carrinho', 'owner', 'item' , 'quantidade' )

class CarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username', read_only=True)
    itemsbuy = serializers.HyperlinkedRelatedField(many=True, view_name='itemcarrinho-detail', read_only=True)
    class Meta:
        model = Carrinho
        fields = ( 'url', 'id', 'itemsbuy', 'owner' ,'subtotal', 'desconto')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    carrinho = serializers.HyperlinkedRelatedField(many=True, view_name='carrinho-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'carrinho')
