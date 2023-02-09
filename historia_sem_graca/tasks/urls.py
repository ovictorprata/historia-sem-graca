from django.urls import path

from . import views

urlpatterns = [
    path("add", views.add_todo),
    path("list", views.list_todos),
    path("get_one_story", views.get_one_story),
    path("<int:pk>/delete", views.remove_story),
    path("update", views.update_story),
]
