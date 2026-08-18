from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent


# Homepage
@app.get("/", include_in_schema=False)
def home():
    return FileResponse(BASE_DIR / "index.html")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


l = {
    "1": "Apple",
    "2": "Banana",
    "3": "Mango",
    "4": "Grapes",
    "5": "Orange"
}

likes = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0
}


# GET - Get all fruits
@app.get("/api/getList/")
def get_list():
    return {
        id: {
            "name": fruit,
            "likes": likes[id]
        }
        for id, fruit in l.items()
    }


# POST - Add fruit
@app.post("/api/postList/")
async def add_fruit(request: Request):
    item = await request.json()

    id = str(len(l) + 1)
    l[id] = item["item"]
    likes[id] = 0

    return {"message": "Fruit added", "data": l}


# DELETE - Delete fruit
@app.delete("/api/deleteList/{id}")
def delete_fruit(id: str):
    if id not in l:
        return {"error": "Fruit not found"}

    del l[id]
    del likes[id]

    return {"message": "Fruit deleted"}


# PUT - Edit fruit
@app.put("/api/updateList/{id}")
async def update_fruit(id: str, request: Request):
    item = await request.json()

    if id not in l:
        return {"error": "Fruit not found"}

    l[id] = item["item"]

    return {"message": "Fruit updated", "fruit": l[id]}


# POST - Like fruit
@app.post("/api/like/{id}")
def like_fruit(id: str):
    if id not in l:
        return {"error": "Fruit not found"}

    likes[id] += 1

    return {
        "fruit": l[id],
        "likes": likes[id]
    }


# GET - Search fruit
@app.get("/api/search/")
def search_fruit(name: str):
    return {
        id: {
            "name": fruit,
            "likes": likes[id]
        }
        for id, fruit in l.items()
        if name.lower() in fruit.lower()
    }