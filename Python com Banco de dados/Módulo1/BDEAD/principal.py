#Criação de banco de dados 

#Problema: calcular a taxa de incidência anual de dengue nos municípios do Rio de Janeiro, no ano de 2018 e 2019

#A taxa de incidência é o número de casos novos divido pelo número de pessoas em risco

#Tarefa: criar um banco de dados para armazenar as informações sobre os casos de dengue e população 

import sqlite3 as conector

conexao = None
cursor = None

try:
    conexao = conector.connect("meu_banco.db")

except conector.DatabaseError as erro:
    print("Erro de banco de dados", erro)

finally:
    
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
