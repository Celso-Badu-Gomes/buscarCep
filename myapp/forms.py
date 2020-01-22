from django import forms
from .models import Endereco

class EnderecoForm(forms.ModelForm):
    
    class Meta:
        model = Endereco
        fields = ('logradouro', 'numero', 'bairro', 'complemento', 'complemento2', 'cidade', 'estado', 'cep',)
        
        
        
        