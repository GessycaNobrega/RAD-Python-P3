 #Para se conectar a um banco de dados SQLite, basta chamar a função connect do módulo sqlite3, passando como argumento o caminho para o arquivo que contém o banco de dados.


#>>> import sqlite3
#>>> conexao = sqlite3.connect('meu_banco.db')

#Isso é o suficiente para termos uma conexão com o banco de dados meu_banco.db e iniciar o envio de comandos SQL para criar tabelas e inserir registros.

#Se quisermos criar um banco de dados em memória, que será criado para toda execução do programa, basta utilizar o comando conexao = sqlite3.connect(':memory:').

import sqlite3 as conector
