from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from db import Base, engine  
import models              
from tasks import router as tasks_router

# --- 2. Crear la Aplicación FastAPI ---
app = FastAPI(title="Gestor de Tareas API") # Definimos la instancia principal

# --- 3. Configuración de CORS ---
origins = [
    "http://localhost:5173", # Puerto de tu React/Vite
    "http://127.0.0.1:5173",
    "https://tu-frontend.onrender.com", # Agrega tu URL de frontend en Render cuando la tengas
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 4. Evento de Startup para crear tablas ---
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

# --- 5. Conectar los Routers ---
app.include_router(tasks_router) 

# --- 6. Endpoint de Prueba ---
@app.get("/")
def read_root():
    return {"mensaje": "¡Backend listo y funcional!"}
