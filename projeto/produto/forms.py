from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = '__all__'
        