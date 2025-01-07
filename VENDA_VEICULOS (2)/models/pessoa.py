class Pessoa:
    def __init__(self, nome, contato, cpf, uf):
        self._nome = nome
        self._contato = contato
        self._cpf = cpf
        self._uf = uf

    @property
    def nome(self):
        return self._nome

    @property
    def contato(self):
        return self._contato
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def uf(self):
        return self._uf

    def __str__(self):
        return f"Nome: {self._nome} \nContato: {self._contato} \nCPF: {self._cpf} \nUF: {self._uf}"
