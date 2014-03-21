from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from todoList.models import TodoList, TodoItem

class IndexView(generic.ListView):
    model = TodoList
    context_object_name = 'todoListe_list'
    template_name = 'todoList/index.html'


#Categories
class DetailCategView(generic.DetailView):
    model = TodoList
    context_object_name = 'todoList'

    def get_context_data(self, **kwargs):
        context = super(DetailCategView, self).get_context_data(**kwargs)
        context['todoListe_list'] = TodoList.objects.all()
        return context
 
class AddCategView(CreateView):
        model = TodoList
        success_url='/todolist/'

class DeleteCategView(DeleteView):
        model = TodoList
        success_url='/todolist/'

class UpdateCategView(UpdateView):
        model = TodoList
        success_url='/todolist/'

#todo
class DetailTodoView(generic.DetailView):
    model = TodoItem

class AddTodoView(CreateView):
        model = TodoItem
        success_url='/todolist/'

	def get_initial(self):
		#todoList = get_object_or_404(TodoList, pk=1)
		categ=TodoList.objects.get(id=self.kwargs['categ'])
		return { 'todoList':categ,}


class DeleteTodoView(DeleteView):
        model = TodoItem
        success_url='/todolist/'

class UpdateTodoView(UpdateView):
        model = TodoItem
        success_url='/todolist/'
