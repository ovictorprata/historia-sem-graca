from historia_sem_graca.accounts.models import User
from historia_sem_graca.accounts.tests import fixtures
from historia_sem_graca.tasks.models import Todo
from django.shortcuts import get_object_or_404
import json

def test_criar_historia_sem_login(client):
    resp = client.post("/api/tasks/add", {"new_task": "minha mãe comprou 5kg de açúcar pq tava na promoção"})
    assert resp.status_code == 401


def test_criar_historia_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/tasks/add", {"new_task": "minha mãe comprou 5kg de açúcar pq tava na promoção"})
    assert resp.status_code == 200


def test_criar_historia_com_login(client, db):
    fixtures.user_jon()
    Todo.objects.create(description="minha mãe comprou 5kg de açúcar pq tava na promoção")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/tasks/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"todos": [{"description": "minha mãe comprou 5kg de açúcar pq tava na promoção", "likes": 0, "id": 1}]}

def test_deleta_historia_com_login_do_proprio_usuario_logado(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))


    Todo.objects.create(description="minha mãe comprou 5kg de açúcar pq tava na promoção")
    Todo.objects.create(description="achei um arquivo no computador chamado torresmo. aí eu abri, e era a foto uma de torresmo.")
    Todo.objects.create(description="queria comer miojo, mas tô com preguiça. conclusão: não vou comer miojo.")

    resp = client.get("/api/tasks/list")
    data = resp.json()
    
    id_para_deletar = data['todos'][0]['id']
    r = client.post(f'/api/tasks/{id_para_deletar}/delete')    

    
    assert resp.status_code == 200
    assert data == {"todos": [
                        {"description": "achei um arquivo no computador chamado torresmo. aí eu abri, e era a foto uma de torresmo.", "done": False, "id": 2},
                        {"description": "queria comer miojo, mas tô com preguiça. conclusão: não vou comer miojo.", "done": False, "id": 3},
                    ]}
    


