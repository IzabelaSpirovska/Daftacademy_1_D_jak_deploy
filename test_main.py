from fastapi import TestClient
from main import app
import pytest

client = TestClient(app)

#--- TASK 0 -----------------------------------------------------------------------------

def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello_world"}

def test_hello_name():
    name = "Kamila"
    response = client.get(f'/hello/{name}')
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}

#--- TASK 1 -----------------------------------------------------------------------------

def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}

#--- TASK 2 -----------------------------------------------------------------------------

def test_method_get():
    response = client.get('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

def test_method_post():
    response = client.post('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "POST"}

def test_method_put():
    response = client.put('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "PUT"}
    
def test_method_delete():
    response = client.delete('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE"}

#--- TASK 3 -----------------------------------------------------------------------------
 
def test_if_id_counter_changes():
    # ARRANGE
    id_counter_pre = app.id_counter
 
    # ACT
    client.post('/patient', json={"name": "X", "surname": "D"})
    id_counter_post = app.id_counter
 
    # ASSERT
    assert id_counter_pre != id_counter_post
    assert id_counter_pre + 1 == id_counter_post
 
 
def test_if_response_correct():
    # ARRANGE
    name = "Kamila"
    surname = "XVB"
    id_counter = app.id_counter
 
    # ACT
    response = client.post('/patient', json={"name": name, "surname": surname})
 
    # ASSERT
    assert response.status_code == 200
    assert response.json() == {"id": id_counter, "patient": {"name": name, "surname": surname}}

#--- TASK 4 -----------------------------------------------------------------------------

def test_if_response_correct_get():
    # ARRANGE
    name = "Kamila"
    surname = "XVB"
    counter = app.id_counter
   
    # ACT with correct pk = counter
    response1 = client.post('/patient', json={"name": name, "surname": surname})
    response2 = client.get('/patient/{pk}', json = counter)
    
    #ASSERT
    assert response1.status_code == 200
    assert response1.json() == {"id": counter, "patient": {"name": name, "surname": surname}}
    assert response2.json() == {"name": name, "surname": surname} 
    
def test_if_response_incorrect_get():
    name = "Kamila"
    surname = "XVB"
    counter = app.id_counter
    wrong_pk = -5
    
    # ACT with wrong pk = -5
    response1 = client.post('/patient', json={"name": name, "surname": surname})
    response2 = client.get('/patient/{pk}', json = wrong_pk)
 
    # ASSERT
    assert response2.status_code == 404
    
