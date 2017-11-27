from rest_framework import serializers
from produtos.models import Produto, Carrinho, ItemCarrinho
from django.contrib.auth.models import User
from django.db.models import Count

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Produto
        fields = ('url', 'owner', 'id' , 'nome', 'descricao', 'imagem', 'valor', 'fator')

class CarrinhoSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Carrinho
            fields = ('url','items')

class ItemCarrinhoSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = ItemCarrinho
            fields = ('url', 'item', 'quantidade')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    produtos = serializers.HyperlinkedRelatedField(many=True, view_name='produto-detail', read_only=True)
    carrinhos = serializers.HyperlinkedRelatedField(many=True, view_name='carrinho-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'produtos', 'carrinhos')
