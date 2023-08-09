from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever
from E_comerce import CarrinhoDeCompras, Produto
from CadastroCliente import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1._inseri_enderecos('Belo Horizonte', 'MG')
cliente2 = Cliente('Maria', 55)
cliente2._inseri_enderecos('Salvador', 'BA')
cliente3 = Cliente('João', 19)
cliente3._inseri_enderecos('Fortaleza', 'CE')

print(cliente1.nome)
cliente1.lista_enderecos()
print(cliente2.nome)
cliente2.lista_enderecos()
print(cliente3.nome)
cliente3.lista_enderecos()

print("###########################################")