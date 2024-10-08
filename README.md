
## Tecnologias Utilizadas
### - Python: Linguagem de programação utilizada
### - VSCode: Editor de codigo utilizado
### - FastAPI: Framework Python focado no desenvolvimento de API’s, tem como principais características ser moderno, rápido e simples
### - SQLite: Banco de dados utilizado
### - SQLite viewer: Extensão do Vscode para visualizar o database Sqlite
### - Thunder Client: Extensão do VSCode utilizada para Salvar e deletar dados da API no SQLite

## Passos para executar o sistema

### - Instalar as extensões do Vscode Thunder Client e SQLite viewer
### - Instalar as dependencias: pip install -r requirements.txt
### - Rodar a aplicação: uvicorn main:app --reload
### Obs: Rotas com metodo GET podem rodar no navergador, exemplo: http://127.0.0.1:8000/personagem ou no Thunder Client selecionando o metodo GET e passando a Url, porem rotas com metodo POST e DELETE so podem ser usadas no Thunder Client passando o metodo e Url

### Obs: Para Salvar Favoritos, no Thunder Client selecione o metodo POST e na Url passe /favoritos/{personagem_id}/{filme_id}/{nave_id}/{veiculo_id}/{especie_id}/{planeta_id}/save
### Use o SQLite viewer para ver os dados salvos e verificar deletes


