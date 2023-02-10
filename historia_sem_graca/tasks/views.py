# coding: utf-8
import json
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc


@csrf_exempt
def add_todo(request):
    todo = todo_svc.add_todo(request.POST["description"])
    return JsonResponse(todo)

def list_random_story(request):
    todos = todo_svc.list_random_story()
    return JsonResponse({"todos": todos})

def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({"todos": todos})

@ajax_login_required
def remove_story(request, pk):
    todo_svc.delete_todo(pk)

@ajax_login_required
def update_story(request):
    id = request.POST.get('id_to_up')
    description = request.POST.get('new_description')
    todo_svc.update_story(id, description)

def like(request):
    id = request.POST.get('id')
    todo_svc.like_story(id)
    return HttpResponse("Hello World!")
    
