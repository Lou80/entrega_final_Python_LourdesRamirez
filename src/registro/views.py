from django.shortcuts import render, redirect

from .forms import UsuarioForm, ConsumoForm, AlimentoForm
from .models import Usuario, Consumo, Alimento


def index(request):
    return render(request, 'registro/index.html')

def about(request):
    return render(request, 'registro/about.html')

def alimento_list(request):
    query = Alimento.objects.all()
    context = {"object_list": query}
    return render(request, "registro/alimento_list.html", context)


def alimento_create(request):
    if request.method == "GET":
        form = AlimentoForm()
    if request.method == "POST":
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro:alimento_list")
    return render(request, "registro/alimento_form.html", {"form": form})


def consumo_list(request):
    query = Consumo.objects.all()
    context = {"object_list": query}
    return render(request, "registro/consumo_list.html", context)


def consumo_create(request):
    if request.method == "GET":
        form = ConsumoForm()
    if request.method == "POST":
        form = ConsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro:consumo_list")
    return render(request, "registro/consumo_form.html", {"form": form})


def usuario_list(request):
    query = Usuario.objects.all()
    context = {"object_list": query}
    return render(request, "registro/usuario_list.html", context)


def usuario_create(request):
    if request.method == "GET":
        form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro:usuario_list")
    return render(request, "registro/usuario_form.html", {"form": form})
