from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import ConsumoForm
from ..models import Consumo


class ConsumoListView(ListView):
    model = Consumo

    def get_queryset(self):
        """
        Obtiene el conjunto de consultas (queryset) para los consumos.

        Si se proporciona un parámetro de búsqueda en la solicitud GET, filtra las consumos
        por el nombre de usuario que contenga
        el término de búsqueda (ignorando mayúsculas y minúsculas).

        Returns:
            QuerySet: Un conjunto de consultas de consumos filtradas según el término de búsqueda,
            o todas las consumos si no se proporciona un término de búsqueda.
        """
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Consumo.objects.filter(
                usuario__nombre__icontains=busqueda
            ) | Consumo.objects.filter(alimento__nombre__icontains=busqueda) | Consumo.objects.filter(alimento__tipo__nombre__icontains=busqueda)
        return Consumo.objects.all()


class ConsumoCreateView(CreateView):
    model = Consumo
    form_class = ConsumoForm
    success_url = reverse_lazy('registro:consumo_list')

    def form_valid(self, form) -> HttpResponse:
        """
        Maneja la lógica cuando el formulario es válido.

        """
        consumo = form.save(commit=False)
        usuario = form.cleaned_data['usuario']
        alimento = form.cleaned_data['alimento']
        cantidad = form.cleaned_data['cantidad']
        fecha_consumo = form.cleaned_data['fecha_consumo']
        consumo.kcal_total = alimento.kcal * cantidad
        consumo.save()
        messages.success(self.request, 'Consumo creado exitosamente')
        return super().form_valid(form)


class ConsumoDetailView(DetailView):
    model = Consumo
