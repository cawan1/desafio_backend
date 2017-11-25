from rest_framework import serializers
from produtos.model import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'imagem', 'valor', 'fator')
