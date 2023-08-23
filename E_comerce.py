'''
Trabalhando com o conceito de agregação
Autor: Felipe Pinto Marinho
Data:08/08/2023
'''
#Exemplo de e-comerce
class CarrinhoDeCompras:
    
    #Inicializador
    def __init__(self):
        self.produtos = []

    #Inserção
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    #Listagem
    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    #Soma Total
    def soma_total(self):
        total = 0 
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:

    #Inicializador
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor