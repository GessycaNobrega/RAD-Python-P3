#Operações CRUD - Principais métodos dos conectores em Python 


#CRIAR TABELA 

import sqlite3
#Abrir uma conexão com o banco de dados 
conn = sqlite3.connect('exemplo.db')
#Criar um cursor para executar comandos SQL
cursor = conn.cursor()
#Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY,
               nome TEXT
               idade INTEGER
               
)
''')



#INSERIR REGISTROS 

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?,?)",
('Alice',30))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?,?)",
('Bob',25))
conn.commit()


#REALIZAR UMA CONSULTA

cursor.execute("SELECT * FROM usuarios")
print("Registros na tabela.")
for registro in cursor.fetchall():
   print(registro)


#ALTERAR UM REGISTRO

cursor.execute("UPDATE usuarios SET idade = ? WHERE nome =?",
(35, 'Alice'
))
conn.commit()

#EXCLUIR UM REGISTRO

cursor.execute("DELETE FROM usuarios WHERE nome = ?",
('Bob',))
conn.commit()
#Fechar o cursor e a conexão
cursor.close()
conn.close()



               