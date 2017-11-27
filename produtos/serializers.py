from rest_framework import serializers
from produtos.models import Produto
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Produto
        fields = ('url', 'owner', 'id' , 'nome', 'descricao', 'imagem', 'valor', 'fator')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    produtos = serializers.HyperlinkedRelatedField(many=True, view_name='produto-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'produtos')
