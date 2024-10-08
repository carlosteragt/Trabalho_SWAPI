from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.get("/planetas")
def get_planetas():
    return get_swapi_data('planets')

@router.get("/planetas/{id}")
def get_planeta(id: int):
    return get_swapi_data('planets', id)

@router.post("/planetas/{id}/save")
def save_planeta(id: int):
    planeta = get_swapi_data('planets', id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO planetas (id, nome, populacao) VALUES (?, ?, ?)", 
                   (id, planeta['name'], planeta['population']))
    conn.commit()
    conn.close()
    return {"message": "Planeta salvo com sucesso!"}

@router.delete("/planetas/{id}/delete")
def delete_planeta(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM planetas WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Planeta não encontrado no banco de dados")
    conn.commit()
    conn.close()
    return {"message": "Planeta deletado com sucesso!"}
