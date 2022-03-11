from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projeto.core.urls')),
    path('produto/', include('projeto.produto.urls')),
    path('estoque/', include('projeto.estoque.urls')),
]
