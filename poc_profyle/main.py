from fastapi import FastAPI
from profyle.fastapi import ProfyleMiddleware

app = FastAPI()
app.add_middleware(ProfyleMiddleware)


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"hello": user_id}


@app.get("/demo/")
async def get_demo():
    return {"hello": "demo"}
