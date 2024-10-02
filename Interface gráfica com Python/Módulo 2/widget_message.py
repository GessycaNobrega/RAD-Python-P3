# O código para gerar uma aplicação com o componente “Message” é dado por:

import tkinter as tk
janela = tk.Tk()
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
janela.mainloop()


# Agora, vamos analisar os principais aspectos do código.

# Linha 4 - É instanciado um componente “Message” com uma mensagem para o usuário.
# Linha 5 - O componente é configurado, determinando a cor do “background” e detalhes sobre a fonte da mensagem.