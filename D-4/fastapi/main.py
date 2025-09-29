from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

 
@app.get('/user/details')
def get():
    return{
        'name': 'lubaba',
        'age': 24,
        'city': 'Guntur',
        'role': 'fromtend developer'

    }

class Iteam(BaseModel):
    name:str
    age:int
    city:str



@app.post('/signup')
def signup(iteam: Iteam):
    return{
        "message":"your details recieved",
        "data":iteam
        
    }

@app.put("/iteam/{name}")
def update(name:str, iteam:Iteam):
        return {'name':name,'update':iteam}