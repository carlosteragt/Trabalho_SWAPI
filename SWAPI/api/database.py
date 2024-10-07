import sqlite3

def get_db_connection():
    conn = sqlite3.connect('swapi.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS personagens (
                        id INTEGER PRIMARY KEY, 
                        nome TEXT, 
                        altura TEXT, 
                        peso TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
                        id INTEGER PRIMARY KEY, 
                        titulo TEXT, 
                        diretor TEXT, 
                        produtor TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS naves (
                        id INTEGER PRIMARY KEY, 
                        nome TEXT, 
                        modelo TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS veiculos (
                        id INTEGER PRIMARY KEY, 
                        nome TEXT, 
                        modelo TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS especies (
                        id INTEGER PRIMARY KEY, 
                        nome TEXT, 
                        homeworld TEXT, 
                        language TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS planetas (
                        id INTEGER PRIMARY KEY, 
                        nome TEXT, 
                        populacao TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS favoritos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        personagem_id INTEGER, 
                        filme_id INTEGER, 
                        nave_id INTEGER, 
                        veiculo_id INTEGER, 
                        especie_id INTEGER, 
                        planeta_id INTEGER)''')

    conn.commit()
    conn.close()
