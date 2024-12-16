


from django.urls import path
from .views import (
    about,
    usuario_create,
    usuario_list,
    consumo_create,
    consumo_list,
    alimento_create,
    alimento_list,
    index,
)

app_name = "registro"

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
     path("alimento/list/", alimento_list, name="alimento_list"),
    path("alimento/create/", alimento_create, name="alimento_create"),
    path("consumo/list/", consumo_list, name="consumo_list"),
    path("consumo/create/", consumo_create, name="consumo_create"),
    path("usuario/list/", usuario_list, name="usuario_list"),
    path("usuario/create/", usuario_create, name="usuario_create"),

]
