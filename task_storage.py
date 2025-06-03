
import json
import asyncio

FILE = "tasks.json"

async def load_contacts():
    try:
        await asyncio.sleep(0.1)  # Simula operación asincrónica
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

async def save_contacts(contacts):
    await asyncio.sleep(0.1)  # Simula operación asincrónica
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)
