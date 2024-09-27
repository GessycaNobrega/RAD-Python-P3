import sqlite3 as conector
from modelos import Municipio, Dengue

conexao = None
cursor = None 

try:

    conexao = conector.connect("meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    with open("dengue_rj.csv") as arquivo:
        arquivo.readline() #descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, casos_2018, casos_2019 = linha.strip().split(';')
            print(codigo, nome, casos_2018, casos_2019)


            municipio = Municipio(codigo, nome)
            comando = '''INSERT INTO Municipio VALUES (:codigo, :nome);'''
            cursor.execute(comando, vars(municipio))

            dengue_2018 = Dengue (codigo, 2018, int(casos_2018))
            dengue_2019 = Dengue (codigo, 2019, int(casos_2019))
            comando = '''INSERT INTO Dengue VALUES (:codigo, :ano, :casos);'''
            cursor.execute(comando, vars(dengue_2018))
            cursor.execute(comando, vars(dengue_2019))

    with open("dengue_rj.csv") as arquivo:
        arquivo.readline() #descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, casos_2018, casos_2019 = linha.strip().split(';')
            print(codigo, nome, casos_2018, casos_2019)


    with open("populacao.csv") as arquivo:
        arquivo.readline() #descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, pop_2018, pop_2019 = linha.strip().split(';')
            print(codigo, nome, pop_2018, pop_2019)
            comando = '''INSERT INTO Populacao VALUES (?,?,?);'''
            cursor.execute(codigo, 2018, pop_2018)
            cursor.execute(codigo, 2019, pop_2019)

            conexao.commit ()

except