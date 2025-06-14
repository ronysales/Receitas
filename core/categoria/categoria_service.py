from core.categoria.categoria_repository import CategoriaRepository
from core.categoria.categoria import Categoria

class CategoriaService:
    def __init__(self):
        self.repository = CategoriaRepository()

    def cadastrar_categoria(self, nome_categoria):
        if not nome_categoria.strip():
            raise ValueError("Nome da categoria é obrigatório.")
        if self.repository.buscar_por_nome(nome_categoria):
            raise ValueError("Categoria já cadastrada.")
        self.repository.salvar(Categoria(nome_categoria))

    def listar_categorias(self):
        return self.repository.listar_todas()

    def buscar_por_nome(self, nome_categoria):
        categoria = self.repository.buscar_por_nome(nome_categoria)
        if not categoria:
            raise ValueError("Categoria não encontrada")
        return categoria

    def atualizar_categoria(self, nome_antigo, nome_novo):
        if not nome_novo.strip():
            raise ValueError("O Nome da categoria é obrigatório")
        if nome_antigo != nome_novo:
            self.repository.atualizar(nome_antigo, nome_novo)
    
    def excluir_categoria(self, nome_categoria):
        self.repository.remover_por_nome(nome_categoria)