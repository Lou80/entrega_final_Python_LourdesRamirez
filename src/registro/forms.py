from django import forms

from .models import Usuario, Consumo, Alimento


class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = "__all__"


class ConsumoForm(forms.ModelForm):
    class Meta:
        model = Consumo
        fields = "__all__"
        widgets = {
            "fecha_consumo": forms.DateInput(attrs={"type": "date"}),
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"