#sintaxe do count : contagem = variavel_string.count(palavra)
with open ('dados.txt','r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    contador = texto.count("Olá")
    print("Total de Olás = ", contador)