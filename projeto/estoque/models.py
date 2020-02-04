from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto



MOVIMENTO = (
	('e', 'entrada'),
	('s', 'saida'),
)

class Estoque(TimeStampedModel):
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
	movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return str(self.pk)

class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque,on_delete=models.CASCADE,related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
    	ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)