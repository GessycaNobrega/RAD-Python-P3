# Para criar um diretório, utilizamos a função mkdir do módulo os, enquanto, para remover um diretório, utilizamos a função rmdir, também do módulo os.


# A sintaxe dessas duas funções são as seguintes:

#Criar: os.mkdir(caminho)
#Remover: os.rmdir(caminho)

#Criar
import os

try:
    os.mkdir("meu_diretorio")
    print("Diretório criado!")
except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print("Descrição", erro)
except FileExistsError as erro:
    print("Diretório já existe.")
    print("Descrição", erro)

print("Término do programa")


#Remover

import os

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido!")
except PermissionError as erro:
    print("Sem permissão para remover diretório")
    print("Descrição", erro)
except FileNotFoundError as erro:
    print("Diretório inexistente.")
    print("Descrição", erro)
except OSError as erro:
    print("Outro erro.")
    print("O diretório está vazio?")
    print("Descrição", erro)

print("Término do programa")


#Listando conteúdo de diretórios
# Sua sintaxe é a seguinte: os.scandir(caminho)


import os 

try: 

    entrada = os.scandir("meu_diretorio")
    for obj in entrada:
        print(obj)
        print("Nome:", obj.name)
        print("Caminho:", obj.path)
        print("É diretório:", obj.is_dir())
        print("É arquivo:", obj.is_file())

        if obj.is_file():
            print("Tamanhanho:", obj.stat().st_size, "B")
            print("======================")
except FileNotFoundError:
    print("O caminho não existe.")
except NotADirectoryError:
    print("O caminho não é de um diretório")
