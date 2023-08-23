'''
Trabalhando com DataClasses
Autor:Felipe Pinto Marinho
Data:09/08/2023
'''
#Carregando o pacote Dataclass
from dataclasses import dataclass, field

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome =sobrenome
    
    def __str__(self):
        class_str = f"{self.__class__.__name__}/{self.nome}{self.sobrenome}"
        return class_str
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, o):
        return self.sobrenome == o.sobrenome
    
@dataclass
class Person:
    nome: str
    sobrenome: str
    ativo: bool = False
    enderecos: list = field(default_factory = list, repr = False, compare = False)
    nome_completo: str = field(default = 'Missing', init = False, repr = False)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} ' f'{self.sobrenome}'
    
    def get_nome_completo(self):
        return self.nome_completo
    
    @property
    def p_get_nome_completo(self):
        return self.nome_completo



john = Person(nome = 'John', sobrenome = 'Doe', ativo = True)
mary = Person('Mary', 'Jane', True, ['R2'] )
print(john)
print(mary)
print(john.get_nome_completo())
print(john.p_get_nome_completo)