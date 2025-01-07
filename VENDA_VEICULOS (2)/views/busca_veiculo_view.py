class BuscaService:
    @staticmethod
    def buscar_veiculo(query, veiculos):
        resultados = [
            v for v in veiculos if query.lower() in v.marca.lower() or query.lower() in v.modelo.lower()
        ]
        if resultados:
            
          
            print(f"Os veiculos encontrados para '{query}' são: \n")
            for veiculo in resultados:
                print(veiculo)
                print('-----------------------------------------------------------')
        else:
            print("Nenhum veículo encontrado.")

