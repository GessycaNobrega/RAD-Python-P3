 #Para se conectar a um banco de dados SQLite, basta chamar a função connect do módulo sqlite3, passando como argumento o caminho para o arquivo que contém o banco de dados.


#>>> import sqlite3
#>>> conexao = sqlite3.connect('meu_banco.db')

#Isso é o suficiente para termos uma conexão com o banco de dados meu_banco.db e iniciar o envio de comandos SQL para criar tabelas e inserir registros.

#Se quisermos criar um banco de dados em memória, que será criado para toda execução do programa, basta utilizar o comando conexao = sqlite3.connect(':memory:').

import sqlite3 as conector

try:
    #Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Execução de um comando... CREAT, SELECT 
    comando = '''CREATE TABLE Pessoa (
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
                );'''
    
    cursor.execute(comando)

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close(
            conexao.close()
        )