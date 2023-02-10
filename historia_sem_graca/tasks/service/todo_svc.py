from ..models import Todo
from django.shortcuts import get_list_or_404, render, redirect


def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    return [todo.to_dict_json() for todo in todos]

def delete_todo(pk):
    # story = get_list_or_404(Todo, pk=pk)
    story = Todo.objects.get(pk=pk)
    story.delete()

def update_story(pk, description):
    story_to_update = Todo.objects.get(pk=pk)
    story_to_update.description = description
    story_to_update.save()



    