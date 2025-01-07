from models.pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nome, contato, cpf, uf):
        super().__init__(nome, 
                         contato, 
                         cpf, 
                         uf)


