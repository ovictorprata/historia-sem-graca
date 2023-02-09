from ..models import Todo
from django.shortcuts import get_list_or_404


def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    return [todo.to_dict_json() for todo in todos]

def delete_todo(pk):
    story = get_list_or_404(Todo, pk=pk)
    story.delete()

    