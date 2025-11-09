from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

# Simpan data sementara di list
items = []

class Item(BaseModel):
    name: str
    price: float
    category: str = "Umum"
    description: str = ""

@app.get("/items")
def get_items():
    return {"message": "Daftar semua item berhasil diambil", "data": items}

@app.post("/items")
def create_item(item: Item):
    new_item = item.dict()
    new_item["id"] = str(uuid.uuid4())
    items.append(new_item)
    return {"message": "Item baru berhasil ditambahkan", "data": new_item}

@app.get("/items/{item_id}")
def get_item(item_id: str):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item dengan id {item_id} tidak ditemukan")

@app.put("/items/{item_id}")
def update_item(item_id: str, updated: Item):
    for item in items:
        if item["id"] == item_id:
            item.update(updated.dict())
            return {"message": "Item berhasil diperbarui", "data": item}
    raise HTTPException(status_code=404, detail="Item tidak ditemukan")

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            del items[i]
            return {"message": f"Item dengan id {item_id} berhasil dihapus"}
    raise HTTPException(status_code=404, detail="Item tidak ditemukan")
