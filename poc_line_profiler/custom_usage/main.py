# main.py
from fastapi import FastAPI

from inmemory import InMemory
from models import Item, ItemKey

import uvicorn # Importar uvicorn explícitamente

app = FastAPI()
inMemory = InMemory()


@app.post("/data", response_model=dict)
async def create_data(item: Item):
    """
    Endpoint to store data in memory with profiling.
    """
    inMemory.store(item.key, item.value)
    return {"message": f"Data stored with key: {item.key}"}


@app.get("/data", response_model=dict)
async def get_data(item: ItemKey):
    value = inMemory.retrieve(item.key)
    return {"message": f"Data retrieved for key: {item.key}", "value": value}


if __name__ == "__main__":
    print("Uvicorn started under kernprof. Close Uvicorn (Ctrl+C) to see profiling.")
    uvicorn.run(app, host="0.0.0.0", port=8000)
