import sqlite3 as conector
from modelo import Veiculo

#Abertura de conexão e aquisição de cursor 
conexao=conector.connect("meu_banco.db")
cursor = conexao.cursor()

#Definicão dos comandos

comando = ''' SELECT * FROM Veiculo; '''
cursor.execute(comando)

#Recuperação dos registros 

reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa:", veiculo.placa, ",Marca:", veiculo.marca)

#fechamento das conexões

cursor.close()
conexao.close()

#Esse script está correto, porém, a saída dele irá trazer na marca o resulto: "Marca 1" e "Marca 2 " e esse número 1 e 2 não se refere ao nome ou sigla da marca, e sim ao ID dessas marcar. O nome mesmo é MARCA A e MARCA B.

#No script 5 será verificado como mostrar o nome da marca