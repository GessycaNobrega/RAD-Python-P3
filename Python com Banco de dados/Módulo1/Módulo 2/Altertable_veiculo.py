import sqlite3 as conector

try:
    #Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Execução de um comando... CREAT, SELECT 
    comando = '''ALTER TABLE Veiculo
                    ADD motor Real;'''
    
    cursor.execute(comando)

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()