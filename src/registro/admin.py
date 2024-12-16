from django.contrib import admin

from .models import Usuario, Consumo, Alimento


@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo")


@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ("alimento__nombre", "cantidad", "fecha_consumo")


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("meta", "email")