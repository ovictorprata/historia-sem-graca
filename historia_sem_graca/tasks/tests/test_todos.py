from historia_sem_graca.accounts.models import User
from historia_sem_graca.accounts.tests import fixtures
from historia_sem_graca.tasks.models import Todo
from model_bakery import baker
from django.shortcuts import get_object_or_404
import json

def test_create_story_without_login(client, db):
    story = baker.make(Todo)
    resp = client.get("/api/tasks/list")
    data = resp.json()

    assert data == {"todos": [
                        {"description": story.description, "likes": story.likes, "id": story.id},
                    ]}

# def test_criar_historia_com_login(client, db):
#     fixtures.user_jon()
#     Todo.objects.create(description="minha mãe comprou 5kg de açúcar pq tava na promoção")

#     client.force_login(User.objects.get(username="jon"))
#     resp = client.get("/api/tasks/list")
#     data = resp.json()

#     assert resp.status_code == 200

def test_delete_any_story_if_user_is_logged(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))

    story1 = baker.make(Todo)
    story2 = baker.make(Todo)

    id_to_delete = story1.id

    client.post(f'/api/tasks/{id_to_delete}/delete')

    response = client.get('/api/tasks/list')
    data = response.json()

    assert response.status_code == 200
    assert data == {"todos": [
                        {"description": story2.description, "likes": story2.likes, "id": story2.id},
                    ]}  

    
def test_delete_any_story_without_login(client, db):
    story1 = baker.make(Todo)
    story2 = baker.make(Todo)

    id_to_delete = story1.id

    client.post(f'/api/tasks/{id_to_delete}/delete')
    response = client.get('/api/tasks/list')
    data = response.json()

    assert data == {"todos": [
                        {"description": story1.description, "likes": story1.likes, "id": story1.id},
                        {"description": story2.description, "likes": story2.likes, "id": story2.id},
                    ]}

def test_update_any_story_if_user_is_logged(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/tasks/list")
    story = baker.make(Todo)
    

    new_description = "minha mãe comprou 100000000000000000kg de açúcar pq tava na promoção"

    client.post("/api/tasks/update", {'id_to_up' : story.id, 'new_description': new_description})

    resp = client.get("/api/tasks/list")
    data = resp.json()
    
    assert resp.status_code == 200
    assert data == {"todos": [
                        {"description": new_description, "likes": story.likes, "id": story.id},
                    ]}

def test_dar_like_sem_estar_logado_aumentando_o_like_em_1(client, db):
    story = baker.make(Todo)

    client.post("/api/tasks/like", {'id' : story.id})

    resp = client.get("/api/tasks/list")
    data = resp.json()
    
    assert data == {"todos": [
                        {"description": story.description, "likes": 1, "id": story.id},
                    ]}

def test_list_random_story_without_login(client, db):
    story = baker.make(Todo)
    resp = client.get("/api/tasks/list")
    data = resp.json()
    assert data == {"todos": [
                        {"description": story.description, "likes": story.likes, "id": story.id},
                    ]}