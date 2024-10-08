from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.get("/veiculos")
def get_veiculos():
    return get_swapi_data('vehicles')

@router.get("/veiculos/{id}")
def get_veiculo(id: int):
    return get_swapi_data('vehicles', id)

@router.post("/veiculos/{id}/save")
def save_veiculo(id: int):
    veiculo = get_swapi_data('vehicles', id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO veiculos (id, nome, modelo) VALUES (?, ?, ?)", 
                   (id, veiculo['name'], veiculo['model']))
    conn.commit()
    conn.close()
    return {"message": "Veículo salvo com sucesso!"}

@router.delete("/veiculos/{id}/delete")
def delete_veiculo(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM veiculos WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Veículo não encontrado no banco de dados")
    conn.commit()
    conn.close()
    return {"message": "Veículo deletado com sucesso!"}
