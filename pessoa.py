#Trabalhando com classes
#Autor: Felipe Pinto Marinho
#Data:04/08/2023

#Importando alguns módulos relevantes
from datetime import datetime
from random import randint

#Criando um molde para minha classe
class Pessoa:

    #Convertendo ano atual em um inteiro
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))
    
    #Uso de um método construtor
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        variavel = "variavel"
        print(variavel)
    
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        
        if self.falando:
            print(f"{self.nome} não pode comer falando.")
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo = False
    
    def falar(self, assunto):
        #Regra de etiqueta
        if self.comendo:
            print(f"{self.nome} não pode falar comendo.")
            return
        
        if self.falando:
            print(f"{self.nome} já está falando.")            
            return
        
        print(f"{self.nome} estar falando sobre {assunto}.")
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não estar falando.")
            return
        
        print(f"{self.nome} parou de falar.")
        self.falando = False
    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
    #Método de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    #Método Estático
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand



