# A função open retorna um objeto do tipo arquivo. Sua forma mais simples de utilização tem a seguinte sintaxe:

arquivo = open (caminho)

# Caminho Absoluto: É a referência completa para se encontrar um arquivo ou diretório. Ele deve começar com uma barra ( / ) ou o rótulo do drive ( C:, D: ...).

#Caminho Relativo: open(“arquivo.txt”), para os casos em que o arquivo está no mesmo diretório do script
 # para os casos em que o arquivo está no diretório acima do script.  open(“../arquivo.txt”)

 # Modos de acesso a um arquivo:

r: leitura (read)

w: escrita (write)

a: acrescentar (append)

#Boas práticas: 

#Ao lidar com arquivos, devemos utilizar a palavra reservada with, disponibilizada pelo Python. Ela garante que o arquivo será fechado adequadamente após utilizarmos o arquivo, não sendo necessário chamar o método close explicitamente. A sintaxe de utilização do with é:

# with open(caminho, modo) as nome: (seu código indentado)


