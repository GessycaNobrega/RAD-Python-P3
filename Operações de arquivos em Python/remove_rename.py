# Função remove:

# Operação de remover um arquivo, que está disponível por meio da função remove do módulo os do Python.

#A função remove tem a seguinte sintaxe: os.remove(caminho)

import os
arquivo_a_remover = "arquivo_a_remover.txt"
try:
    os.remove(arquivo_a_remover)
    print(f"O arquivo {arquivo_a_remover} foi removido com sucesso.")
except FileNotFoundError:
    print(f"O arquivo {arquivo_a_remover} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao remover o arquivo {e}.")

# Função rename

#A função rename tem a seguinte sintaxe:  os.rename(origem, destino)

import os
nome_antigo = "arquivo_antigo.txt"
nome_novo = "arquivo_novo.txt"
try:
    os.rename(nome_antigo, nome_novo)
    print(f"O arquivo {nome_antigo} foi renomeado para {nome_novo}.")
except FileNotFoundError:
    print(f"O arquivo {nome_antigo} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao renomear o arquivo {e}.")
