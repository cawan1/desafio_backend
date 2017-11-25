from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer

@api_view(['GET', 'POST'])
def produto_list(request, format=None):
        """
        Lista todos os produtos ou cria um novo produto
        """
        
        if request.method == 'GET':
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ProdutoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def produto_detail(request, pk, format=None):
    """
    Selecionar , editar, excluir produtos
    """
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
