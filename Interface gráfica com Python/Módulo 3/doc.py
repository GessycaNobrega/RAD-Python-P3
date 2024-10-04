#Aprenderemos como estabelecer conexões, executar consultas SQL e manipular dados diretamente da linguagem Python. Descubra como essa integração pode otimizar a gestão de dados e agilizar processos de análise e visualização.


CREATE TABLE public."AGENDA"
(
   id integer NOT NULL,
   nome text COLLATE pg_catalog."default" NOT NULL,
   telefone char(12) COLLATE pg_catalog."default" NOT NULL
)
TABLESPACE pg_default;
ALTER TABLE public."AGENDA"
OWNER to postgres;


#Para testar se a criação da tabela está correta, pode-se inserir um registro da seguinte maneira:

INSERT INTO public."AGENDA"( id, nome, telefone)
VALUES (1, 'teste 1', '02199999999');


#Em seguida, fazemos uma consulta na tabela:

SELECT * FROM public." AGENDA";


#Para instalá-lo, basta digitar na linha de comando do python:

pip install psycopg2



#Criação de tabela

#Este primeiro código mostra como criar uma tabela a partir do python. É uma alternativa em relação a criar a tabela usando o PostgreSQL.

import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()




#Inserção de dados na tabela

import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password=" senha123" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""") 
conn.commit() 
print("Inserção realizada com sucesso!"); 8conn.close()





#Seleção de dados na tabela


import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password=" senha123" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 8 conn.commit() 9 print("Seleção realizada com sucesso!"); 
conn.close()


#Atualização de dados na tabela


import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password="senha123" , host="127.0.0.1" , port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
print("Consulta antes da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
#Atualização de um único registro 
cur.execute("""Update public."AGENDA" set "telefone"='02188888888' where "id"=1""") 
conn.commit() 
print("Registro Atualizado com sucesso! ")
cur = conn.cursor()
print(" Consulta depois da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
conn.commit() 
print("Seleção realizada com sucesso!");
conn.close()



#Exclusão de dados na tabela

import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password="senha123" , host="127.0.0.1" , port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""Delete from public."AGENDA" where "id"=1""") 
conn.commit() 
cont=cur.rowcount 
print(cont, "Registro excluído com sucesso!") 
print("Exclusão realizada com sucesso!"); 
conn.close()
