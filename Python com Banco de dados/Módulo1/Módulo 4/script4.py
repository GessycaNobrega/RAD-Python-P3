#vamos buscar os veículos e suas respectivas marcas, utilizando junção de tabelas.


import sqlite3 as conector
from modelo import Veiculo

 # Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

 # Definição dos comandos
comando = '''SELECT * FROM Veiculo;'''
cursor.execute(comando)

 # Recuperação dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

 # Fechamento das conexões
cursor.close()
conexao.close()


#Resultado da saída:
# D:Banco de dados> & C:python.exe "d:/Banco de dados/script19_1.py"
# Placa: AAA0001 , Marca: 1
# Placa: BAA0002 , Marca: 1
# Placa: CAA0003 , Marca: 2
# Placa: DAA0004 , Marca: 2


#Verifique no console que os valores do atributo marca são seus respectivos ids, 1 e 2. Isso ocorre porque no banco de dados armazenamos apenas uma referência à chave primária da entidade Marca.



#E se quisermos substituir o id das marcas pelos seus respectivos nomes? Para isso, precisamos realizar uma junção das tabelas Veículo e Marca no comando SELECT.


#O comando SELECT para junção de duas tabelas tem a seguinte sintaxe:
#SELECT tab1.col1, tab1.col2, tab2.col1… FROM tab1 JOIN tab2 ON tab1.colN = tab2.colM;