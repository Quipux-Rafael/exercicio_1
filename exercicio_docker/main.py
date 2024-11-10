import ast
import os
from datetime import datetime
import uuid
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongodb_host = os.getenv("MONGODB_HOST", "localhost")
mongodb_port = int(os.getenv("MONGODB_PORT", 27017))
client = MongoClient(f"mongodb://{mongodb_host}:{mongodb_port}")
db = client.python_app
collection = db.listas_no_ordenadas

@app.get("/lista-ordenada/")
def lista_ordenada(lista_no_ordenada):
    """
    Ordena una lista de valores proporcionada como cadena y devuelve la lista ordenada junto con la hora actual del sistema.

    Args:
        lista_no_ordenada (str): Una cadena que representa una lista de valores desordenados. Ejemplo: "[3, 1, 4, 1, 5]".

    Returns:
        dict: Un diccionario que contiene:
            - 'hora_sistema' (str): Hora actual del sistema en formato "DD/MM/YYYY HH:MM:SS".
            - 'lista_ordenada' (list): Lista de valores ordenados.

    Raises:
        ValueError: Si la cadena proporcionada no puede evaluarse como una lista válida.

    Ejemplo:
        /lista-ordenada/?lista_no_ordenada=[3, 1, 4, 1, 5]
        {
            'hora_sistema': '07/11/2024 14:52:13',
            'lista_ordenada': [1, 1, 3, 4, 5]
        }
    """
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
    """
        Verifica el estado de salud del servicio y devuelve una respuesta simple.

        Returns:
            str: Un mensaje indicando que el servicio está en funcionamiento, en este caso, "Ok".

        Ejemplo:
            /healthcheck
            "Ok"
        """
    return "Ok"

@app.get("/guardar-lista-no-ordenada")
def guarda_lista_no_ordenada(lista_no_ordenada):
    try:
        lista_no_ordenada = ast.literal_eval(lista_no_ordenada)
    except:
        raise  ValueError(f"Erro na lista")

    hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    unique_id = str(uuid.uuid4())

    try:
        collection.insert_one({
            "id": unique_id,
            "hora_sistema": hora_atual,
            "lista_no_ordenada": lista_no_ordenada
        })
        return {"msg": f"Erro ao guardar no mongoDB"}
    except:
        raise ValueError

