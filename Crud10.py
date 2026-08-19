from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []  # List to store todo items

class Todo(BaseModel):
    id: int
    title:str
    completed:bool
    
# Create an API
@app.post("/todos")
def create_todo(todo:Todo):  # todo:Todo -> At least our model will be check.
    todos.append(todo)
    return {"message": "TODO added", "data": todo}

# Create get API
@app.get("/todos")
def get_todos():
    return todos


# For getting a single piece of data
@app.get("/todos/{todo_id}")  # Based on the id we will get the data
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

# Update existing data
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Data Updated",
                "data": updated_todo
            }
    return {"error": "Todo not found"}

#####################################################################

# Delete existing data
# Delete method based on id
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id : int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{"message": "Data Deleted"}
        
    return {"error": "Todo not found"}
        