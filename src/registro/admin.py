from django.contrib import admin

from .models import Usuario, Consumo, Alimento, Categoria

admin.site.register(Categoria)

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "kcal")


@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "fecha_consumo","alimento__nombre", "cantidad"  )


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "meta_diaria_kcal")