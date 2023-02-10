from django.urls import path

from . import views

urlpatterns = [
    path("add", views.add_todo),
    path("list", views.list_todos),
    path("list_non_logged", views.list_random_story),
    path("like", views.like),
    path("<int:pk>/delete", views.remove_story),
    path("update", views.update_story),
]
