class Receita:
    def __init__(self, id=0, nome_receita="", ingredientes="", modo_preparo="", categoria=""):
        self.id = id
        self.nome_receita = nome_receita
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.categoria = categoria