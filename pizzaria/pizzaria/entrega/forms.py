# coding: utf-8

from django  import forms 
ModelForm 

from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        
class ObservacaoClienteForm(forms.Form):
    obs = forms.CharField()
