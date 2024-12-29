from django.urls import path

from .views import index
from .views_models import categoria, alimento, usuario, consumo

app_name = "registro"

urlpatterns = [path('', index, name='index')]

urlpatterns += [
    path('categoria/list/', categoria.categoria_list, name='categoria_list'),
    path('categoria/create/', categoria.categoria_create, name='categoria_create'),
    path('categoria/update/<int:pk>', categoria.categoria_update, name='categoria_update'),
    path('categoria/detail/<int:pk>', categoria.categoria_detail, name='categoria_detail'),
    path('categoria/delete/<int:pk>', categoria.categoria_delete, name='categoria_delete'),
]

urlpatterns += [
    path('alimento/list/', alimento.AlimentoListView.as_view(), name='alimento_list'),
    path('alimento/create/', alimento.AlimentoCreateView.as_view(), name='alimento_create'),
    path('alimento/update/<int:pk>', alimento.AlimentoUpdateView.as_view(), name='alimento_update'),
    path('alimento/detail/<int:pk>', alimento.AlimentoDetailView.as_view(), name='alimento_detail'),
    path('alimento/delete/<int:pk>', alimento.AlimentoDeleteView.as_view(), name='alimento_delete'),
]

urlpatterns += [
    path('usuario/list/', usuario.UsuarioListView.as_view(), name='usuario_list'),
    path('usuario/create/', usuario.UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuario/update/<int:pk>', usuario.UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuario/detail/<int:pk>', usuario.UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuario/delete/<int:pk>', usuario.UsuarioDeleteView.as_view(), name='usuario_delete'),
]

urlpatterns += [
    path('consumo/list/', consumo.ConsumoListView.as_view(), name='consumo_list'),
    path('consumo/create/', consumo.ConsumoCreateView.as_view(), name='consumo_create'),
    path('consumo/detail/<int:pk>', consumo.ConsumoDetailView.as_view(), name='consumo_detail'),
]


