import requests


def get_categorias():
    # Primero se hace la peticion a la API Rest
    response = requests.get('http://127.0.0.1:3000/api/categoria/list/')
    # Verificar la respuesta
    if response.status_code == 200:
        return response.json()


def get_productos():
    # Primero se hace la peticion a la API Rest
    response = requests.get('http://127.0.0.1:3000/api/producto/list/')
    # Verificar la respuesta
    if response.status_code == 200:
        return response.json()
