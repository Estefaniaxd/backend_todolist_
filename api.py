from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from db import Base, engine  
import models              
from tasks import router as tasks_router

models.Base.metadata.create_all(bind=engine)

# --- 2. Crear la Aplicación FastAPI ---
app = FastAPI(title="Gestor de Tareas API") # Definimos la instancia principal

# --- 3. Configuración de CORS ---
origins = [
    "http://localhost:5173", # Puerto de tu React/Vite
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 4. Conectar los Routers ---
app.include_router(tasks_router) 

# --- 5. Endpoint de Prueba ---
@app.get("/")
def read_root():
    return {"mensaje": "¡Backend listo y funcional!"}
