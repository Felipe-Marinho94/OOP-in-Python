'''''
Trabalhando com encapsulamento
Autor:Felipe Pinto Marinho
Data:08/08/2023

Tópico estudados:
Public, Private, Protected
_ Private/Protected
__ Private (INST._NOMEDACLASSE__nomeatributo)
'''''

#Molde para classe base de dados
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    #Getter
    @property
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Mário')
bd.inserir_cliente(3, 'Rose')
bd.__dados = "Outra coisa"
print(bd.__dados)
bd.lista_clientes()
print(bd._BaseDeDados__dados)