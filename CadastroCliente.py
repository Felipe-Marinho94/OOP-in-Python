'''
Trabalhando com o conceito de composição de classes
Autor:Felipe Pinto Marinho
Data:09/08/2023
'''

#Classe cliente
class Cliente:

    #Inicializador
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    #Inseri endereço
    def _inseri_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    
    #lista endereços
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    #Apagar cliente
    def __del__(self):
        print(f"{self.nome} FOI APAGADO.")
    

#Classes Endereço
class Endereco:
    
    #Inicializador
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    #Apagar endereço
    def __del__(self):
        print(f"{self.cidade}/{self.estado} FOI APAGADO.")
