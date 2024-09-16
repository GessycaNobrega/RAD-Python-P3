with open ('dados.txt','r', encoding='utf-8') as arquivo:
    contador = 0
    print('Representação do arquivo')
    for linha in arquivo:
        print(repr(linha))
        if linha:
            contador += 1
            print ("Total de linhas = ", contador)

with open ('dados.txt','r', encoding='utf-8') as arquivo:
    contador = 0
    print ('Representação do arquivo após strip')
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
        print ("Total de linhas =", contador)