from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed = Task.objects.filter(is_completed=True)
    context = {
        'tasks':tasks,
        'completed':completed
    }
    return render(request, 'home.html',context)