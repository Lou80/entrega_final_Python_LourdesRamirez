from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import AlimentoForm
from ..models import Alimento


class AlimentoListView(ListView):
    model = Alimento

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Alimento.objects.filter(nombre__icontains=busqueda)
        return Alimento.objects.all()


class AlimentoCreateView(CreateView):
    model = Alimento
    form_class = AlimentoForm
    success_url = reverse_lazy('registro:alimento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Alimento creado exitosamente')
        return super().form_valid(form)


class AlimentoUpdateView(UpdateView):
    model = Alimento
    form_class = AlimentoForm
    success_url = reverse_lazy('registro:alimento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Alimento actualizado exitosamente')
        return super().form_valid(form)


class AlimentoDetailView(DetailView):
    model = Alimento


class AlimentoDeleteView(DeleteView):
    model = Alimento
    success_url = reverse_lazy('registro:alimento_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Alimento eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
