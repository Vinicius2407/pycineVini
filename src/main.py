from typing import Union
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import (
     CORSMiddleware
)
from typing import List

import sys
sys.path.append("src\model")
import models

import sys
sys.path.append("src\database")
import database

import sys
sys.path.append("src\controller")
import userController


#TODO: testar para ver se o banco não esta sendo apagado toda vez que inicia o servidor
models.database.Base.metadata.create_all(bind=database.engine)

#Dependency DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Usando isso o svelte conseguirá acessar o backend
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chamadas HTTPs
@app.get("/users/list", status_code=200)
def read_users():
    user = userController.read_users()
    users= []
    for i in user:
        users.append({
                "id": i[0], 
                "name": i[1], 
                "email": i[2], 
                "password": i[3]
            },
        )  
         
    return users

@app.post("/user/create")
async def create_user(request: Request):
    data = await request.json()
    userCreate = userController.create_user({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
        });
    if userCreate:
        return userCreate
    else:
        raise HTTPException(status_code=400, detail="User not created")


@app.put("/user/update", status_code=200)
async def update_user(request: Request):
    data = await request.json()
    resultado = userController.update_user({
        "id": data["id"],
        "name": data["name"],
        "email": data["email"],
        })
    return {"message": resultado}


@app.delete("/users/delete/{id}", status_code=200)
async def delete_user(id: str):
    user = userController.delete_user(id)    
    return user


@app.get("/")  # HTTP GET
async def home():
    return {"msg": "Hello"}

# rodar o fastapi:
# uvicorn src.main:app --reload

