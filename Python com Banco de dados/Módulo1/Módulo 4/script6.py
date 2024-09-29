import sqlite3 as conector
from modelo import Veiculo

#Abertura de conexão e aquisição de cursor 
conexao=conector.connect("meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT 
                Veiculo.placa, Veiculo.ano, Veiculo.cor,
                Veiculo.motor, Veiculo.proprietario,
                Marca.nome FROM Veiculo JOIN ON Marca.id = Veiculo.marca;'''
cursor.execute(comando)