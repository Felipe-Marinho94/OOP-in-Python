'''
Realizando Associação entre classes
Autor:Felipe Pinto Marinho
Data:08/08/2023
'''

#Criando algumas classes
class Escritor:
    
    #Método Inicializador
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    
    #Getter
    @property
    def nome(self):
        return self.__nome
    
    #Getter para ferramenta
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
    

class Caneta:

    #Método Inicializador
    def __init__(self, marca):
        self.__marca = marca
    
    #Getter
    @property
    def marca(self):
        return self.__marca
    
    #Escrever
    def escrever(self):
        print("Caneta está escrevendo...")

class MaquinaDeEscrever:
    def escrever(self):
        print("Máquina está escrevendo...")
