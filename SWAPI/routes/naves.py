from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.get("/naves")
def get_naves():
    return get_swapi_data('starships')

@router.get("/naves/{id}")
def get_nave(id: int):
    return get_swapi_data('starships', id)

@router.post("/naves/{id}/save")
def save_nave(id: int):
    nave = get_swapi_data('starships', id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO naves (id, nome, modelo) VALUES (?, ?, ?)", 
                   (id, nave['name'], nave['model']))
    conn.commit()
    conn.close()
    return {"message": "Nave salva com sucesso!"}

@router.delete("/naves/{id}/delete")
def delete_nave(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM naves WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Nave não encontrada no banco de dados")
    conn.commit()
    conn.close()
    return {"message": "Nave deletada com sucesso!"}
