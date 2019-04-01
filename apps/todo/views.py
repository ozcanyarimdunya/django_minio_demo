from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models, forms


class TodoList(ListView):
    queryset = models.Todo.objects.all()
    template_name = 'list.html'


class TodoCreate(CreateView):
    queryset = models.Todo.objects.all()
    form_class = forms.TodoForm
    template_name = 'create.html'
    success_url = reverse_lazy('todo:list')


class TodoDetail(DetailView):
    queryset = models.Todo.objects.all()
    template_name = 'detail.html'


class TodoUpdate(UpdateView):
    queryset = models.Todo.objects.all()
    form_class = forms.TodoForm
    template_name = 'update.html'
    success_url = reverse_lazy('todo:list')


class TodoDelete(DeleteView):
    queryset = models.Todo.objects.all()
    form_class = forms.TodoForm
    template_name = 'delete.html'
    success_url = reverse_lazy('todo:list')
