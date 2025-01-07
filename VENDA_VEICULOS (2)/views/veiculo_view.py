import os
import json
from models.veiculo import Veiculo
from models.vendedor import Vendedor

class VeiculoService:
    DATA_DIR = "data"  
    DATA_FILE_JSON = os.path.join(DATA_DIR, "veiculos.json")
    DATA_FILE_TXT = os.path.join(DATA_DIR, "veiculos.txt")

    @staticmethod
    def _garantir_diretorio_e_arquivos():
        # Criar o diretório, se não existir
        os.makedirs(VeiculoService.DATA_DIR, exist_ok=True)

        # Criar o arquivo JSON, se não existir
        if not os.path.exists(VeiculoService.DATA_FILE_JSON):
            with open(VeiculoService.DATA_FILE_JSON, "w") as file:
                json.dump([], file)

        # Criar o arquivo TXT, se não existir
        if not os.path.exists(VeiculoService.DATA_FILE_TXT):
            open(VeiculoService.DATA_FILE_TXT, "w").close()

    @staticmethod
    def carregar_veiculos():
        VeiculoService._garantir_diretorio_e_arquivos()
        try:
            with open(VeiculoService.DATA_FILE_JSON, "r") as file:
                return [
                    Veiculo(
                        v["Marca"],
                        v["Modelo"],
                        v["Ano"],
                        v["Preco"],
                        
                        Vendedor(v["Nome do Vendedor"], v["Contato do Vendedor"], v["CPF"], v["UF"])
                    )
                    for v in json.load(file)
                ]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_veiculos(veiculos):
        VeiculoService._garantir_diretorio_e_arquivos()

        # Salvar em JSON
       
        with open(VeiculoService.DATA_FILE_JSON, "w") as file:
            json.dump(
                [
                    {
                        "Marca": v.marca,
                        "Modelo": v.modelo,
                        "Ano": v.ano,
                        "Preco": v.preco,
                        "Nome do Vendedor": v.vendedor.nome,
                        "Contato do Vendedor": v.vendedor.contato,
                        "CPF": v.vendedor.cpf,
                        "UF": v.vendedor.uf
                        
                    }
                    for v in veiculos
                ],
                file,
                indent=4,
            )

        # Salvar em TXT
        with open(VeiculoService.DATA_FILE_TXT, "w") as file:
            for v in veiculos:
                file.write(str(v) + "\n---\n")