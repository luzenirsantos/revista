from django.contrib import admin
from .models import *


class ColecaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cod_colecao')
	list_filter = ('nome','cod_colecao')

class CaixaAdmin(admin.ModelAdmin):
	list_display = ('numero_caixa', 'cor', 'etiqueta', 'colecao')
	list_filter = ('numero_caixa','colecao')

class RevistaAdmin(admin.ModelAdmin):
	list_display = ('colecao','numero_edicao','caixa')
	list_filter = ('colecao', 'numero_edicao', 'caixa')

class AmigoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone')

class EmprestimoAdmin(admin.ModelAdmin):
	list_display = ('amigo', 'data_emprestimo', 'data_devolucao', 'devolvido')
	list_filter = ('data_devolucao','devolvido')

admin.site.register(Colecao, ColecaoAdmin)
admin.site.register(Caixa, CaixaAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Revista - Emprestimo'