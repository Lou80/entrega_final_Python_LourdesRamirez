import unicodedata

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone




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

class Categoria(models.Model):
    """Categorías de alimentos"""

    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Alimento'
        verbose_name_plural = 'Categorías de Alimento'


class Alimento(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    tipo = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='categoría',
        db_index=True
    )
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
        base = f'{self.nombre}: {self.kcal} kcal'
        if self.tipo:
            return f'{base} ({self.tipo})'
        return base

    class Meta:
        unique_together = ('tipo', 'nombre')
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    meta_diaria_kcal = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='imagenes_perfil', blank=True, null=True)
    def __str__(self):
        return self.nombre


class Consumo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, verbose_name='paciente')
    alimento = models.ForeignKey(Alimento, on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    kcal_total = models.PositiveIntegerField(editable=False)
    fecha_consumo = models.DateField(default=timezone.now, editable=False)

    class Meta:
        ordering = ('-fecha_consumo',)

    def __str__(self):
        return f"Paciente {self.usuario} consumió {self.cantidad} porción/es de {self.alimento} el {self.fecha_consumo}"


