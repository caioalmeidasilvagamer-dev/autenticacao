import sqlite3
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

def criar_tabela():
    with sqlite3.connect("users.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                nome    TEXT NOT NULL,
                email   TEXT UNIQUE NOT NULL,
                senha   TEXT NOT NULL,
                cargo   TEXT NOT NULL, 
                criado_em TEXT DEFAULT (datetime('now', '-3 hours'))
            )
        """)

def cadastrar_usuario(nome, email, senha, cargo):
    senha_hash = generate_password_hash(senha)
    with sqlite3.connect("users.db") as conn:
        conn.execute('''INSERT INTO usuarios (nome, email, senha, cargo) VALUES (?,?,?,?)''',
                 (nome, email, senha_hash, cargo))
        
def buscar_usuario(email):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.execute("""
            SELECT * FROM usuarios WHERE email = ?""", 
            (email,))
        resultado = cursor.fetchone()
        return resultado if resultado else None
    
def verificar_login(email, senha):
    usuario = buscar_usuario(email)
    if not usuario:
        return None
    senha_certo = check_password_hash(usuario[3], senha)
    return usuario if senha_certo else None