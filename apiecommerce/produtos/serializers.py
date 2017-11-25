from rest_framework import serializers
from produtos.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('sku', 'nome', 'descricao', 'imagem', 'valor', 'fator')
