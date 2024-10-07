from fastapi import FastAPI
from routes import status, personagens, filmes, naves, veiculos, especies, planetas, favoritos
from api.database import initialize_database

app = FastAPI()
initialize_database()

app.include_router(status.router)
app.include_router(personagens.router)
app.include_router(filmes.router)
app.include_router(naves.router)
app.include_router(veiculos.router)
app.include_router(especies.router)
app.include_router(planetas.router)
app.include_router(favoritos.router)
