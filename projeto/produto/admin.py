from django.contrib import admin
from .models import Produto

# admin.site.register(Produto)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'importado', 
        'ncm', 
        'preco', 
        'estoque',
        'estoque_minimo', 
    )
    search_fields = ('produto',)
    list_filter = ('importado',)
