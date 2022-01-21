from django.urls import path

from AppCoder.views import Curso_CreateView, Curso_DeleteView, Curso_DetailView, Curso_ListView, Curso_UpdateView, inicio

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', Curso_ListView.as_view(), name='cursos'),
    path('cursos/add', Curso_CreateView.as_view(), name='curso_add'),
    path('curso/update/<pk>', Curso_UpdateView.as_view(), name='curso_update'),
    path('curso/delete/<pk>', Curso_DeleteView.as_view(), name='curso_delete'),
    path('curso/view/<pk>', Curso_DetailView.as_view(), name='curso_view')
]