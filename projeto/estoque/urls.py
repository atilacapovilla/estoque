from django.urls import path, include
from projeto.estoque import views as v

app_name = 'estoque'

entrada_patterns = [
    path('', v.EstoqueEntradaList.as_view(), name='estoque_entrada_list'),
    # path('<int:pk>/', v.EstoqueEntradaDetail.as_view(), name='estoque_entrada_detail'),
    path('add/', v.estoque_entrada_add, name='estoque_entrada_add'),
]

saida_patterns = [
    path('', v.EstoqueSaidaList.as_view(), name='estoque_saida_list'),
    # path('saida/<int:pk>/', v.EstoqueSaidaDetail.as_view(), name='estoque_saida_detail'),
    path('add/', v.estoque_saida_add, name='estoque_saida_add'),
]

urlpatterns = [
    path('<int:pk>/', v.EstoqueDetail.as_view(), name='estoque_detail'),
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),
]