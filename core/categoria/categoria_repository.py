import sqlite3
from core.categoria.categoria import Categoria

class CategoriaRepository:
    def __init__(self, db_path='dbReceitas.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._criar_tabela()

    def _criar_tabela(self):
        query = '''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_categoria TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def salvar(self, categoria: Categoria):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO categorias (nome_categoria) VALUES (?)", (categoria.nome_categoria,))
        self.conn.commit()

    def listar_todas(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM categorias")
        rows = cursor.fetchall()
        return [Categoria(row["nome_categoria"]) for row in rows]

    def buscar_por_nome(self, nome_categoria):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM categorias WHERE nome_categoria = ?", (nome_categoria,))
        row = cursor.fetchone()
        return Categoria(row["nome_categoria"]) if row else None
