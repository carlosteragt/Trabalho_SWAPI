from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.get("/personagens")
def get_personagens():
    return get_swapi_data('people')

@router.get("/personagens/{id}")
def get_personagem(id: int):
    return get_swapi_data('people', id)

@router.post("/personagens/{id}/save")
def save_personagem(id: int):
    personagem = get_swapi_data('people', id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO personagens (id, nome, altura, peso) VALUES (?, ?, ?, ?)", 
                   (id, personagem['name'], personagem['height'], personagem['mass']))
    conn.commit()
    conn.close()
    return {"message": "Personagem salvo com sucesso!"}

@router.delete("/personagens/{id}/delete")
def delete_personagem(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personagens WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Personagem não encontrado no banco de dados")
    conn.commit()
    conn.close()
    return {"message": "Personagem deletado com sucesso!"}
