from fastapi import APIRouter, HTTPException
from api.swapi import get_swapi_data
from api.database import get_db_connection

router = APIRouter()

@router.post("/favoritos/{personagem_id}/{filme_id}/{nave_id}/{veiculo_id}/{especie_id}/{planeta_id}/save")
def save_favorito(personagem_id: int, filme_id: int, nave_id: int, veiculo_id: int, especie_id: int, planeta_id: int):

    personagem = get_swapi_data('people', personagem_id)
    filme = get_swapi_data('films', filme_id)
    nave = get_swapi_data('starships', nave_id)
    veiculo = get_swapi_data('vehicles', veiculo_id)
    especie = get_swapi_data('species', especie_id)
    planeta = get_swapi_data('planets', planeta_id)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO favoritos (personagem_id, filme_id, nave_id, veiculo_id, especie_id, planeta_id) VALUES (?, ?, ?, ?, ?, ?)", 
            (personagem_id, filme_id, nave_id, veiculo_id, especie_id, planeta_id)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

    return {"message": "Favorito salvo com sucesso!"}

@router.get("/getFavorito")
def get_favorito():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM favoritos ORDER BY id DESC LIMIT 1")
    favorito = cursor.fetchone()
    
    if favorito is None:
        raise HTTPException(status_code=404, detail="Nenhum favorito encontrado.")

    personagem = get_swapi_data('people', favorito[1])
    filme = get_swapi_data('films', favorito[2])
    nave = get_swapi_data('starships', favorito[3])
    veiculo = get_swapi_data('vehicles', favorito[4])
    especie = get_swapi_data('species', favorito[5])
    planeta = get_swapi_data('planets', especie['homeworld'].split("/")[-2])

    response = {
        "personagem": {
            "nome": personagem['name'],
            "ano_de_nascimento": personagem['birth_year']
        },
        "filme": {
            "nome": filme['title'],
            "numero_do_filme": filme['episode_id']
        },
        "nave": {
            "nome": nave['name'],
            "modelo": nave['model']
        },
        "veiculo": {
            "nome": veiculo['name'],
            "modelo": veiculo['model']
        },
        "especie": {
            "nome": especie['name'],
            "planeta_natal": planeta['name'],
            "linguas_faladas": especie['language']
        },
        "planeta": {
            "nome": planeta['name'],
            "populacao": planeta['population']
        },
        "alunos": [
            {
                "nome": "Carlos Henrique Vieira da Silva",
                "matricula": "98023522"
            },
            {
                "nome": "Maicon de Souza Lucas",
                "matricula": "98023052"
            },
            {
                "nome": "Leonardo Isaias das Chagas",
                "matricula": "98024147"
            }
        ],
        "curso": "Sistemas de Informação",
        "universidade": "Univás",
        "periodo": "6º"
    }

    conn.close()
    return response
