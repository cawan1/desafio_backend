from django.db import models
from produtos.models import Produto
#from django.db.models import Sum

# Create your models here.

class ItemCarrinho(models.Model):
    #item = models.ForeignKey(Produto)
    item = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
  #  valor_produto = Produto.valor
#    valor = models.FloatField()
#    fator = models.CharField(max_length=1)

#PRODUTOS_DISPONIVEIS=[(item) for item in Produto.objects.all()]

class Carrinho(models.Model):
    owner = models.ForeignKey('auth.User', related_name='carrinho', on_delete=models.CASCADE, blank=True)
    items = models.ManyToManyField(ItemCarrinho) #, related_name='itemcarrinho', on_delete=models.CASCADE)    
    #items = models.ManyToManyField(Produto, through=ItemCarrinho, blank=True)
    #items = models.CharField(choices=PRODUTOS_DISPONIVEIS, blank=True, max_length=100)
    subtotal = models.DecimalField(max_digits=50, decimal_places=2, default=0.00, blank=True)
    desconto = models.FloatField()
