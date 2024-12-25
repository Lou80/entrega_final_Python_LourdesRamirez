from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import ConsumoForm
from ..models import Usuario, Consumo


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
                vendedor__usuario__username__icontains=busqueda
            ) | Consumo.objects.filter(registro__nombre__icontains=busqueda)
        return Consumo.objects.all()


class ConsumoCreateView(CreateView):
    model = Consumo
    form_class = ConsumoForm
    success_url = reverse_lazy('registro:consumo_list')

    def get_form_kwargs(self) -> dict:
        """
        Sobrescribe el método get_form_kwargs para incluir el usuario actual en los argumentos de
        palabra clave del formulario.
        Returns:
            dict: Los argumentos de palabra clave para el formulario, incluyendo el usuario actual.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form) -> HttpResponse:
        """
        Maneja la lógica cuando el formulario es válido.

        Este método se llama cuando el formulario ha sido validado correctamente.
        1. Guarda la consumo sin confirmar la transacción en la base de datos.
        2. Asigna el vendedor basado en el usuario actual.
        3. Calcula el precio total de la consumo.
        4. Actualiza el stock del registro y guarda tanto el registro como la consumo.

        Args:
            form (Form): El formulario validado que contiene los datos de la consumo.

        """
        consumo = form.save(commit=False)
        consumo.vendedor = Usuario.objects.get(usuario=self.request.user)
        registro = form.cleaned_data['registro']
        cantidad = form.cleaned_data['cantidad']
        consumo.precio_total = registro.precio * cantidad
        registro.stock -= cantidad
        registro.save()
        consumo.save()
        messages.success(self.request, 'Consumo creada exitosamente')
        return super().form_valid(form)


class ConsumoDetailView(DetailView):
    model = Consumo
