import requests
from fastapi import HTTPException

def get_swapi_data(endpoint, id=None):
    url = f"https://swapi.dev/api/{endpoint}/"
    if id:
        url += f"{id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail=f"Recurso {endpoint} com ID {id} não encontrado na SWAPI")
