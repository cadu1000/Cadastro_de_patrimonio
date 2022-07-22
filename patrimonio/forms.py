from core.models import Patrimonio
from django import forms

class InserePatrimonioForm(forms.ModelForm):
    class Meta:
        # Modelo Base
        model = Patrimonio

        # Campos que estarão no form
        fields = [
            'nome_objeto',
            'etiqueta',
            'usuario',
            'setor',
            'valor',
            'dt_cadastro',
            'observacao'
        ]
        # Campos que não estarão no form (somente exemplo...)
        #exclude = [
        #    'descrição'
        #]

