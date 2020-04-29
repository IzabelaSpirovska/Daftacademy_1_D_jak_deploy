from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
 
class HelloNameResp(BaseModel):
    message: str
 
class Patient(BaseModel):
    name: str
    surname: str
 
class Response(BaseModel):
    id: int
    patient: Patient
   
app = FastAPI()
app.id_counter = 0
app.data: Dict[int, Patient] = {}
 
 
#--- TASK 0 -----------------------------------------------------------
 
@app.get('/')
def hello_world():
    return{'message': 'Hello_world'}
 
@app.get('/hello/{name}', response_model = HelloNameResp)
def hello_name(name: str):
    return HelloNameResp(message = f'Hello {name}')
 
#--- TASK 1 -----------------------------------------------------------
 
@app.get('/')
def hello_world():
    return {'message': 'Hello World during the coronavirus pandemic!'}
 
#--- TASK 2 -----------------------------------------------------------
 
@app.get('/method')
def method_get():
    return {'method': 'GET'}
 
@app.post('/method')
def method_post():
    return {'method': 'POST'}
 
@app.put('/method')
def method_put():
    return {'method': 'PUT'}
 
@app.delete('/method')
def method_delete():
    return {'method': 'DELETE'}
 
#--- TASK 3 -----------------------------------------------------------
 
@app.post('/patient', response_model = Response)
def patient_position(pt: Patient):
    patient_with_id = Response(id = app.id_counter, patient = pt)
    app.id_counter += 1
    return patient_with_id
 
#--- TASK 4 -----------------------------------------------------------
 
@app.get('/patient/{pk}')
def next_patient(pk: int):
    patient = app.data.get(pk)
    if patient is not None:
        return patient
    else:
        raise HTTPException(status_code = 404, detail = 'Not found')
