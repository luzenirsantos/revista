from django.db import models
from django.utils import timezone
from django.forms import ModelForm


TIPO_GRUPO = (
    ('Escola','Escola'),
    ('Prédio','Prédio'),
)

class Colecao(models.Model):
	class Meta:
		verbose_name_plural="coleções"

	nome = models.CharField('Nome', max_length=50)
	cod_colecao = models.CharField('Número da coleção', max_length=6)
	
	def __str__(self):
		return self.nome

class Caixa(models.Model):
	numero_caixa = models.CharField('Número da caixa', max_length=4)
	cor = models.CharField('Cor', max_length=15)
	etiqueta = models.CharField('Etiqueta', max_length=20)
	colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.numero_caixa

class Revista(models.Model):
	numero_edicao = models.CharField('Edição', max_length=10)
	colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
	ano = models.IntegerField('Ano')
	caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
	
	def __str__(self):
		return "{}, ({})".format(self.colecao, self.numero_edicao)

class Amigo(models.Model):
	nome = models.CharField('Nome', max_length=50)
	telefone = models.CharField('Telefone', max_length=11)
	grupo = models.CharField('Grupo', max_length=15, choices=TIPO_GRUPO)
	
	def __str__(self):
		return self.nome
		
class Emprestimo(models.Model):
	amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
	revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
	data_emprestimo = models.DateField('Data do empréstimo')
	data_devolucao = models.DateField('Data da devolução')
	devolvido = models.BooleanField()