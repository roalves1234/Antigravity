from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from execution.form_app.models.database import save_nome, init_db
import os

router = APIRouter()

# Directories
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "views", "templates")
templates = Jinja2Templates(directory=templates_dir)

@router.on_event("startup")
def on_startup():
    try:
        init_db()
        print("Tabela 'teste' verificada/criada com sucesso.")
    except Exception as e:
        print("Erro ao inicializar o banco de dados:", e)

@router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def submit_form(request: Request, nome: str = Form(...)):
    message = None
    status_class = ""
    try:
        save_nome(nome)
        message = f"Nome '{nome}' salvo com sucesso!"
        status_class = "success"
    except Exception as e:
        message = f"Erro ao salvar: {str(e)}"
        status_class = "error"
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "message": message,
        "status_class": status_class
    })
