#Desenvolvimento de CRUD
#Autor: Felipe Pinto Marinho
#Data: 15/08/2023
#CREATE
#READ
#UPDATE
#DELETE

#Carregando alguns pacotes importantes
import mysql.connector

#Conexão com o bd
conexao = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='joaogrilo',
    database ='bdyoutube' 
)

#Criação de um cursor
cursor = conexao.cursor()

#Criação de CRUD
'''
#CREATE
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() ##Editar banco de dados
#resultado = cursor.fetchall() #Ler banco de dados

#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#conexao.commit() ##Editar banco de dados
resultado = cursor.fetchall() #Ler banco de dados
print(resultado)

#UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #Edita o banco de dados
'''

#DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #Edita o banco de dados

#Fechando o cursor e conexão
cursor.close()
conexao.close()