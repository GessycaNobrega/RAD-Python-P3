arquivo = open('dados.txt','r', encoding='utf-8')

conteudo = arquivo.read()

print("Tipo de conteúdo: ", type(conteudo))


print ('Conteúdo retorado pelo read: ')

print(repr(conteudo)) #reproduz o conteúdo 

arquivo.close()