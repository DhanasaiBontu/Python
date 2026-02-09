from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel,Field

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    description:Optional[str]
    completed:bool=False

@app.get("/todos")
def show():
    return todos

@app.post("/todos",status_code=201)
def post(todo1:Todo):
    todos.append(todo1)
    return todo1

@app.get("/todos/{id}")
def showTask(id:int):
    for i in todos:
        if(id==i.id):
            return i
    raise HTTPException(
        status_code=404,
        detail=f"{id} id not found!"
    )

@app.put("/todos/{id}")
def update(id:int,todo:Todo):
    for index, task in enumerate(todos):
        if task.id == id:
            todos[index] = todo
            return todo
    raise HTTPException(
        status_code=404,
        detail=f"{id} id not found!"
    )

@app.delete("/todos/{id}")
def delete(id:int):
    for task in todos:
        if(task.id==id):
            todos.remove(task)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"{id} id not found!"
    )