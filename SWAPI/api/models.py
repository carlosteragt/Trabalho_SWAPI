from pydantic import BaseModel

class Personagem(BaseModel):
    nome: str
    altura: str
    peso: str

class Filme(BaseModel):
    titulo: str
    diretor: str
    produtor: str

class Nave(BaseModel):
    nome: str
    modelo: str

class Veiculo(BaseModel):
    nome: str
    modelo: str

class Especie(BaseModel):
    nome: str
    homeworld: str
    language: str

class Planeta(BaseModel):
    nome: str
    populacao: str
