from django.db import models
from produtos.models import Produto
#from django.db.models import Sum

# Create your models here.

#class ItemCarrinho(models.Model):
    #item = models.ForeignKey(Produto)
#    carrinho = models.ForeignKey(Carrinho, related_name='items')
#    item = models.ForeignKey(Produto, related_name='item')
#    quantidade = models.PositiveIntegerField(default=1)
  #  valor_produto = Produto.valor
#    valor = models.FloatField()
#    fator = models.CharField(max_length=1)

#PRODUTOS_DISPONIVEIS=[(item) for item in Produto.objects.all()]

class Carrinho(models.Model):
    owner = models.ForeignKey('auth.User', related_name='carrinho', on_delete=models.CASCADE, blank=True)
    itemsbuy = models.CharField(max_length=100) #ItemCarrinho, related_name='items') #, on_delete=models.CASCADE)    
    #items = models.ManyToManyField(Produto, through=ItemCarrinho, blank=True)
    #items = models.CharField(choices=PRODUTOS_DISPONIVEIS, blank=True, max_length=100)
    #subtotal = models.DecimalField(max_digits=50, decimal_places=2, default=0.00, blank=True)
    #desconto = models.FloatField()


class ItemCarrinho(models.Model):
    owner = models.ForeignKey('auth.User', related_name='itemcarrinho', on_delete=models.CASCADE, blank=True)
    #item = models.ForeignKey(Produto)
    cart = models.ForeignKey(Carrinho, related_name='items')
    item = models.ForeignKey(Produto, related_name='item')
    quantidade = models.PositiveIntegerField(default=1)
                      #  valor_produto = Produto.valor
                      #    valor = models.FloatField()
                      #    fator = models.CharField(max_length=1)
