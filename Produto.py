#Criando um molde para uma classe de produtos

class Produto:
    
    #Método construtor
    def __init__(self, nome, preço):
        
        self.nome = nome
        self.preço = preço
    
    #Método para adcionar um desconto
    def desconto(self, percentual):
        self.preço -= (percentual/100) * self.preço
    
    #Getter nome
    @property
    def nome(self):
        return self._nome
    
    #Setter nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    #Getter preço
    @property
    def preço(self):
        return self._preço
    
    #Setter preço
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        
        self.preço = valor

#Criando alguns produtos
p1 = Produto("camiseta", 50)
p1.desconto(10)
print(p1.preço)

p2 = Produto("caneca", 15)
p2.desconto(10)
print(p2.preço)