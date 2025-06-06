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
