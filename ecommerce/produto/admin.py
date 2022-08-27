from django.contrib import admin
from . import models


class VariacaoInLine(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado']
    # display_links = ['nome', 'descricao_curta', 'preco_marketing', 'preco_marketing_promocional']
    inlines = [
        VariacaoInLine
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)

