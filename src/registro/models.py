import unicodedata

from django.core.exceptions import ValidationError
from django.db import models

TIPOS_ALIMENTO = [
    ("proteína", "Proteína"),
    ("carbohidrato", "Carbohidrato"),
    ("grasa", "Grasa"),
    ("vegetal", "Vegetal")
]


def normalizar_texto(texto: str) -> str:
    """Transforma el texto a una forma normalizada NFD
    (Normalization Form Decomposition).
    Esto significa que los caracteres compuestos,
    como las letras con tildes o diacríticos,
    se descomponen en su forma base y sus marcas diacríticas separadas.
    Ej: la letra "é" se descompone en "e" + un carácter de tilde combinable (U+0301).
    Convierte la cadena en bytes usando la codificación ASCII.
    Si un carácter no puede representarse en ASCII (por ejemplo, una "ñ" o una "é"),
    se ignora debido al parámetro "ignore".
    Luego, convierte los bytes resultantes nuevamente a una cadena de texto utilizando la codificación UTF-8."""
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto.lower()


class Alimento(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPOS_ALIMENTO)
    kcal = models.PositiveIntegerField()

    def validate_unique(self, exclude=None):
        """
        Valida que el modelo cumpla con las restricciones de unicidad definidas,
        incluyendo las personalizadas. Método propio de Django.
        """
        super().validate_unique(exclude)
        texto_normalizado = normalizar_texto(self.nombre)
        if Alimento.objects.filter(nombre__iexact=texto_normalizado).exists():
            raise ValidationError("Ya existe. Se ha considerado tildes y mayúsculas.")

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    meta_diaria_kcal = models.PositiveIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.nombre

class Consumo(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    fecha_consumo = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    def calorias_totales(self):
        if self.alimento:
            return self.cantidad * self.alimento.kcal
        return 0
    def __str__(self):
        return f"{self.usuario} consumió {self.cantidad} porción/es de {self.alimento} el {self.fecha_consumo}"


