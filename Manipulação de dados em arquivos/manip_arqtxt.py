#Manipulando arquivo-texto em Python

#Situação-problema: Você foi contratado por uma editora para desenvolver um programa que ajude na revisão de textos. A editora recebe frequentemente textos de autores que contêm inconsistências no uso de maiúsculas e minúsculas, o que dificulta o processo de edição e publicação.

#passos esperados no programa:

#Captura de dados: o programa deve solicitar ao usuário que insira várias frases ou parágrafos pelo console. A entrada de dados deve continuar até o usuário digitar "sair", indicando que deseja encerrar a inserção e salvar o arquivo.

#Criação e armazenamento: o texto inserido deve ser salvo em um arquivo chamado meu_arquivo.txt.

#Manipulação do arquivo: o programa deve abrir o arquivo salvo, ler o conteúdo e converter todas as letras para maiúsculas.

#Sobrescrever o arquivo original: após a manipulação, o texto alterado deve ser usado para sobrescrever o arquivo original, garantindo que o arquivo contenha apenas o texto formatado.

def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)
    
    with open("meu_arquivo.txt", "w") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")
    
    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("meu_arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper())  # Exemplo de manipulação: converter para maiúsculas
    
    with open("meu_arquivo.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    
    print("O arquivo foi sobrescrito com os dados modificados.")
 
if __name__ == "__main__":
    main()