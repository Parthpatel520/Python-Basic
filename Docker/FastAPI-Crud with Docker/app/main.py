from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {}

# Model
class Item(BaseModel):
    name: str
    price: int
    
# Create
@app.post("/items/")
def create_item(id:int, request:Item):
    items[id] = request
    return {"message": "Item Created", "data": request}

