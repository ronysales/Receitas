from core.receita.receita_repository import ReceitaRepository
from core.receita.receita import Receita

class ReceitaService:
    def __init__(self):
        self.repository = ReceitaRepository()

    def cadastrar_ou_atualizar(self, receita: Receita):
        if not receita.nome_receita:
            raise ValueError("Nome da receita é obrigatório.")
        self.repository.salvar(receita)

    def listar_receitas(self):
        return self.repository.listar_todas()

    def obter_receita_por_id(self, id):
        receita = self.repository.buscar_por_id(id)
        if not receita:
            raise ValueError("Receita não encontrada.")
        return receita
