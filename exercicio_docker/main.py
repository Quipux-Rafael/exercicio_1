import ast
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/lista-ordenada/")
def lista_ordenada(lista_no_ordenada):
    try:
        lista_no_ordenada = ast.literal_eval(lista_no_ordenada)
        lista_ordenada = sorted(lista_no_ordenada)
    except:
        raise ValueError

    hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return {
        "hora_sistema": hora_atual,
        "lista_ordenada": lista_ordenada
    }


@app.get("/healthcheck")
def healthcheck():
    return "Ok"