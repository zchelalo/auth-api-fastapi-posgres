from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home = APIRouter()

@home.get('/', tags=['home'])
def message():
  return HTMLResponse('<h1>Hola mundo</h1>')