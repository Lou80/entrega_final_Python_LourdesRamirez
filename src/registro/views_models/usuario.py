from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import UsuarioForm
from ..models import Usuario


class UsuarioListView(ListView):
    model = Usuario

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Usuario.objects.filter(usuario__username__icontains=busqueda)
        return Usuario.objects.all()


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('registro:usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente')
        return super().form_valid(form)


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('registro:usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario actualizado exitosamente')
        return super().form_valid(form)


class UsuarioDetailView(DetailView):
    model = Usuario


class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('registro:usuario_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Usuario eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
