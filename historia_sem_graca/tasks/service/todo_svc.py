from ..models import Todo
from django.shortcuts import get_list_or_404, render, redirect


def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    return [todo.to_dict_json() for todo in todos]

def delete_todo(request, pk):
    # story = get_list_or_404(Todo, pk=pk)
    story = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        story.delete()
        return redirect('tasks/list')
    return render(request, 'your_template.html', {'story': story})

    