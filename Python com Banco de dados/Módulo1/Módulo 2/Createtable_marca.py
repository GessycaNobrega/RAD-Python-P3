import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    with conector.connect("./meu_banco.db") as conexao:
        cursor = conexao.cursor()

        # Execução de um comando... CREATE TABLE
        comando = '''CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        sigla CHAR(2) NOT NULL
                    );'''
        
        cursor.execute(comando)

        # Efetivação do comando
        conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados:", err)


finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
        


