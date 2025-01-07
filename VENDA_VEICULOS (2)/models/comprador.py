from models.pessoa import Pessoa

class Comprador(Pessoa):
    def __init__(self, nome, contato,):
        super().__init__(nome, contato)

