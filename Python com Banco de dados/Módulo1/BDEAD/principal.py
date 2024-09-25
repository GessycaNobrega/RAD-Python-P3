#Criação de banco de dados 

#Problema: calcular a taxa de incidência anual de dengue nos municípios do Rio de Janeiro, no ano de 2018 e 2019

#A taxa de incidência é o número de casos novos divido pelo número de pessoas em risco

#Tarefa: criar um banco de dados para armazenar as informações sobre os casos de dengue e população 

import sqlite3 as conector

conexao = None
cursor = None

# try:
conexao = conector.connect("meu_banco.db")
conexao.execute("PRAGMA foreign_keys  = on")
cursor = conexao.cursor()

    # comando = '''CREATE TABLE IF NOT EXISTS Municipio (
    #                 codigo INTEGER NOT NULL,
    #                 nome VARCHAR(32) NOT NULL,
    #                 PRIMARY KEY (codigo)
    #                 );'''
    
    # cursor.execute(comando)


    # comando = '''CREATE TABLE IF NOT EXISTS Populacao (
    #                 codigo INTEGER NOT NULL,
    #                 ano INTEGER NOT NULL,
    #                 PRIMARY KEY (codigo,ano),
    #                 FOREIGN KEY (codigo) REFERENCES Municipio(codigo)
    #                 );'''
    
    # cursor.execute(comando)


    # comando = '''CREATE TABLE IF NOT EXISTS Dengue (
    #                 codigo INTEGER NOT NULL,
    #                 ano INTEGER NOT NULL,
    #                 PRIMARY KEY (codigo,ano),
    #                 FOREIGN KEY (codigo) REFERENCES Municipio(codigo)
    #                 );'''
    
    # cursor.execute(comando)

    # conexao.commit()

comando = '''ALTER TABLE populacao
                ADD populacao INTEGER NOT NULL;'''
cursor.execute(comando)
conexao.commit()

# except conector.OperationalError as erro:
#     print("Erro operacional", erro)
# except conector.DatabaseError as erro:
#     print("Erro de banco de dados", erro)

