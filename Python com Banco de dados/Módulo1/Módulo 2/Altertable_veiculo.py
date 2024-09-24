import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    with conector.connect("./meu_banco.db") as conexao:
        cursor = conexao.cursor()

        # Execução de um comando para adicionar coluna
        comando = '''ALTER TABLE Veiculo
                     ADD COLUMN motor REAL;'''
        
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