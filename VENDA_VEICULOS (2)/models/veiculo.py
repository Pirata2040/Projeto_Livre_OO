from models.vendedor import Vendedor

class Veiculo:
    def __init__(self, marca, modelo, ano, preco, vendedor):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._preco = preco
        self._vendedor = vendedor

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    @property
    def preco(self):
        return self._preco

    @property
    def vendedor(self):
        return self._vendedor

    def __str__(self):
        return (
            f"Nome: {self._marca}\n"
            f"Modelo: {self._modelo}\n"
            f"Ano: {self._ano}\n"
            f"Preco: R$ {self._preco}\n"
            f"{self._vendedor}"
        )
