from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.get("/especies")
def get_especies():
    return get_swapi_data('species')

@router.get("/especies/{id}")
def get_especie(id: int):
    return get_swapi_data('species', id)

@router.post("/especies/{id}/save")
def save_especie(id: int):
    especie = get_swapi_data('species', id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO especies (id, nome, homeworld, language) VALUES (?, ?, ?, ?)", 
                   (id, especie['name'], especie['homeworld'], especie['language']))
    conn.commit()
    conn.close()
    return {"message": "Espécie salva com sucesso!"}

@router.delete("/especies/{id}/delete")
def delete_especie(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM especies WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Espécie não encontrada no banco de dados")
    conn.commit()
    conn.close()
    return {"message": "Espécie deletada com sucesso!"}
