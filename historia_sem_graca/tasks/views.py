# coding: utf-8
import json
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc


@csrf_exempt
@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST["description"])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({"todos": todos})

@ajax_login_required
def remove_story(request, pk):
    todo_svc.delete_todo(pk)
    return HttpResponse("Hello, World!")

    
