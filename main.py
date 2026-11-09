from fastapi import FastAPI
from pydantic import BaseModel

# 1. Inicializamos la aplicación FastAPI
app = FastAPI(
    title="Mi Primera API en el Reto",
    description="API simple explicada paso a paso con FastAPI, Docker y Ngrok",
    version="1.0.0"
)

# Base de datos simulada (una lista en memoria)
items_db = ["Ordenador", "Teclado", "Ratón"]

# Modelo de datos para validar cuando alguien añade un producto nuevo
class NuevoItem(BaseModel):
    nombre: str

# MÉTODO 1: Ruta principal de bienvenida (GET)
@app.get("/", summary="Saludo inicial")
def inicio():
    return {"mensaje": "¡Hola! La API está funcionando correctamente."}

# MÉTODO 2: Consultar todos los elementos de la lista (GET)
@app.get("/items", summary="Obtener lista de objetos")
def obtener_items():
    return {"total": len(items_db), "items": items_db}

# MÉTODO 3: Añadir un elemento nuevo a la lista (POST)
@app.post("/items", summary="Añadir un objeto nuevo")
def agregar_item(item: NuevoItem):
    items_db.append(item.nombre)
    return {"mensaje": f"Se ha añadido '{item.nombre}' con éxito.", "lista_actualizada": items_db}
