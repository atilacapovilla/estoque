from django.contrib import admin
from .models import Estoque, EstoqueEntrada, EstoqueSaida, EstoqueItens

class EstoqueItensInLine(admin.TabularInline):
    model = EstoqueItens
    extra = 0
@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInLine,)
    list_display = (
        '__str__',
        'movimento',
        'nf', 
        'funcionario',
    )
    search_fields = ('nf',)
    list_filter = ('funcionario', 'movimento',)
    date_hierarchy = ('created')

@admin.register(EstoqueSaida)
class EstoqueSaidapythonAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInLine,)
    list_display = (
        '__str__',
        'movimento',
        'nf', 
        'funcionario',
    )
    search_fields = ('nf',)
    list_filter = ('funcionario', 'movimento',)
    date_hierarchy = ('created')