#Verifique no console, do resultado do script4, que os valores do atributo marca são seus respectivos ids, 1 e 2. Isso ocorre porque no banco de dados armazenamos apenas uma referência à chave primária da entidade Marca.

#E se quisermos substituir o id das marcas pelos seus respectivos nomes?

# Resposta: Para isso, precisamos realizar uma junção das tabelas Veículo e Marca no comando SELECT. O comando SELECT para junção de duas tabelas tem a seguinte sintaxe: SELECT tab1.col1, tab1.col2, tab2.col1… FROM tab1 JOIN tab2 ON tab1.colN = tab2.colM;


#Primeiro, definimos quais colunas serão retornadas utilizando a sintaxe nome_tabela.nome_coluna, depois indicamos as tabelas que desejamos juntar e, por último, indicamos como alinhar os registros de cada tabela, ou seja, quais são os atributos que devem ser iguais (colN e colM).


#No exemplo a seguir, vamos criar um script de forma que o Veículo tenha acesso ao nome da Marca, não ao id.

import sqlite3 as conector
from modelo import Veiculo

 # Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

 # Definição dos comandos 
comando = ''' 
 SELECT Veiculo.placa, Veiculo.ano, Veiculo.cor, Veiculo.motor, Veiculo.proprietario, Marca.nome 
 FROM Veiculo 
 JOIN Marca ON Marca.id = Veiculo.marca;'''
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

# D:\Banco de dados> & C:/python.exe "d:/Banco de dados/script19_2.py" Placa: AAA0001 , Marca: Marca A
# Placa: BAA0002 , Marca: Marca A
# Placa: CAA0003 , Marca: Marca B
# Placa: DAA0004 , Marca: Marca B