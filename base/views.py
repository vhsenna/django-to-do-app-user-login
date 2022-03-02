from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'task_list'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task_detail'
