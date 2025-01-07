import os
from views.veiculo_view import VeiculoService
from views.busca_veiculo_view import BuscaService
from models.vendedor import Vendedor
from models.veiculo import Veiculo

class MenuController:
    @staticmethod
    def menu_principal():
        veiculos = VeiculoService.carregar_veiculos()

        while True:
            print("\n=== Sistema de Venda/Compra de Veículos ===")
            print("1. Ver veículos disponíveis para Compra")
            print("2. Pesquisar um veículo")
            print("3. Anunciar um veículo")
            print("4. Sair")
            print("============================================\n")
            escolha = input("Escolha uma opção: ")
            os.system('clr||clear')

            print('===================================||===============================')
            if escolha == "1":
                print('Estes são os veículos cadastrados no sistema, BOAS COMPRAS! \n')
                
                for veiculo in veiculos:
                    print(veiculo)
                    print('=======================||====================================')
                
            elif escolha == "2":
                
                query = input("Digite o marca ou modelo do veículo para buscar: ")
                print('=======================||========================================')
                BuscaService.buscar_veiculo(query, veiculos)
                
            elif escolha == "3":

                marca = input("Marca do veículo: ")
                modelo = input("Modelo do veículo: ")
                ano = input("Ano do veículo: ")
                preco = input("Preço do veículo: ")
                vendedor_nome = input("Nome do vendedor: ")
                vendedor_contato = input("Contato do vendedor: ")
                vendedor_cpf = input("CPF do Vendedor: ")
                vendedor_uf = input("UF do Vendedor: ")
                print('----------------------------------------------------------')
                vendedor = Vendedor(vendedor_nome, vendedor_contato, vendedor_cpf, vendedor_uf)
                veiculo = Veiculo(marca, modelo, ano, preco, vendedor)
                veiculos.append(veiculo)
                VeiculoService.salvar_veiculos(veiculos)
                print("Veículo anunciado com sucesso!")
                print('=======================||======================================')
            elif escolha == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

