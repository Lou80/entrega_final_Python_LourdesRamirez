from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import CategoriaForm
from ..models import Categoria

# **** CATEGORIA - LIST VIEW


def categoria_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Categoria.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = Categoria.objects.all()
    return render(request, 'registro/categoria_list.html', {'object_list': queryset})


# **** CATEGORIA - CREATE VIEW


def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente')
            return redirect('registro:categoria_list')
    return render(request, 'registro/categoria_form.html', {'form': form})


# **** CATEGORIA - UPDATE VIEW


def categoria_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    if request.method == 'GET':
        form = CategoriaForm(instance=query)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente')
            return redirect('registro:categoria_list')
    return render(request, 'registro/categoria_form.html', {'form': form})


# **** CATEGORIA - DETAIL VIEW


def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    return render(request, 'registro/categoria_detail.html', {'object': query})


# **** CATEGORIA - DELETE VIEW


def categoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        messages.success(request, 'Categoría eliminada exitosamente')
        return redirect('registro:categoria_list')
    return render(request, 'registro/categoria_confirm_delete.html', {'object': query})
