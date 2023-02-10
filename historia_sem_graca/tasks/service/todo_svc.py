from ..models import Todo
import random
import time


def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    return [todo.to_dict_json() for todo in todos]

def list_random_story():
    all_stories = Todo.objects.all()
    random_story = random.choice(all_stories)
    time.sleep(1)
    return [random_story.to_dict_json()]

def delete_todo(pk):
    story = Todo.objects.get(pk=pk)
    story.delete()

def update_story(pk, description):
    story_to_update = Todo.objects.get(pk=pk)
    story_to_update.description = description
    story_to_update.save()

def like_story(pk):
    story = Todo.objects.get(pk=pk)
    story.likes += 1
    story.save()



    