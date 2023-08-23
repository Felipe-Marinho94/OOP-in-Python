'''
Abordando o conceito de Herança Simples
Autor:Felipe Pinto Marinho
Data:09/08/2023

Resumo:
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
'''
class Pessoa:
    #Inicializador
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    #Falar
    def falar(self):
        print(f'{self.nomeclasse} Falando...')
   

class Cliente(Pessoa):
    
    #Comprar
    def comprar(self):
        print(f"{self.nomeclasse} Comprando...")

class Aluno(Pessoa):
    #Estudar
    def estudar(self):
        print(f"{self.nomeclasse} Estudando...")