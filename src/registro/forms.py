from django import forms

from .models import Usuario, Consumo, Alimento, Categoria

def validar_nombre(nombre: str):
    if len(nombre) < 3:
        raise forms.ValidationError('La longitud debe ser mayor a 3 caracteres')
    if not nombre.isalpha():
        raise forms.ValidationError('Debe contener caracteres alfabéticos')
    return nombre

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')
        return validar_nombre(nombre)

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