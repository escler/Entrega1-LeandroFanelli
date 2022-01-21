from msilib.schema import ListView
from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from AppCoder.models import Curso

def inicio(request):
    return render(request, 'AppCoder/inicio.html')


class Curso_ListView(ListView):
    
    model = Curso
    template_name = 'AppCoder/cursos.html'
    context_object_name = 'cursos'
    
class Curso_DetailView(DetailView):
    model = Curso
    template_name = 'AppCoder/ver_curso.html'
    


class Curso_CreateView(CreateView):
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Curso_UpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Curso_DeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')