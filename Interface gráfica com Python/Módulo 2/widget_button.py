#O código para gerar uma aplicação com o componente “Button” é dado por: 

import tkinter as tk
contador = 0
def contador_label(lblRotulo):
   def funcao_contar():
      global contador
      contador = contador + 1
      lblRotulo.config(text=str(contador))
      lblRotulo.after(1000, funcao_contar)
      funcao_contar()
janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()


#Este programa vai gerar uma janela com um contador de segundos – que utiliza um componente “label” – e um componente botão com a mensagem “Clique aqui para interromper a contagem”.



# As linhas mais importantes deste código são:

# Linha 14 - Chamada para a função “contador_label”, função que faz a contagem dos segundos e a atualização dos dados do componente “label”.
# Linha 15 - Criação de uma instância do componente “botão” com uma mensagem, largura do componente e o estabelecimento de um comportamento, no caso, fechar a janela, quando o usuário pressionar o botão.