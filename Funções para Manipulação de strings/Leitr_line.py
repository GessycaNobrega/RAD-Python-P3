arquivo = open('dados.txt','r', encoding='utf-8')

conteudo = arquivo.readline()

print("Tipo de conteúdo: ", type(conteudo))


print ('Conteúdo retorado pelo read: ')

print(repr(conteudo)) #reproduz o conteúdo 

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado: ")
print(repr(proximo_conteudo))

arquivo.close()