from django.db import models

# Create your models here.

FATOR_CHOICES = (
    ('A', 'FATOR A'),
    ('B', 'FATOR B'), 
    ('C', 'FATOR C'),
)

class Produto(models.Model):
    owner = models.ForeignKey('auth.User', related_name='produtos', on_delete=models.CASCADE, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens', blank=True)
    valor = models.FloatField()
    fator = models.CharField(choices=FATOR_CHOICES, max_length=1)
