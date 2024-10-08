from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.get("/filmes")
def get_filmes():
    return get_swapi_data('films')

@router.get("/filmes/{id}")
def get_filme(id: int):
    return get_swapi_data('films', id)

@router.post("/filmes/{id}/save")
def save_filme(id: int):
    filme = get_swapi_data('films', id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO filmes (id, titulo, diretor, produtor) VALUES (?, ?, ?, ?)", 
                   (id, filme['title'], filme['director'], filme['producer']))
    conn.commit()
    conn.close()
    return {"message": "Filme salvo com sucesso!"}

@router.delete("/filmes/{id}/delete")
def delete_filme(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM filmes WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Filme não encontrado no banco de dados")
    conn.commit()
    conn.close()
    return {"message": "Filme deletado com sucesso!"}
