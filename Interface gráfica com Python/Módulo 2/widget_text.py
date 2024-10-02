#O próximo exemplo apresenta como usar o widget “Text”. O código para gerar uma aplicação com o componente “Text” é dado por:

import tkinter as tk
janela = tk.Tk()
T = tk.Text(janela, height=2, width=30)
T.pack()
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
tk.mainloop()


# Agora, vamos analisar os principais aspectos do código.

# Linha 3 - É feita uma instância do componente “Text”.
# Linha 5 - É inserido um texto na instância do componente “text”, que será exibido na tela. Observe que o texto é separado em duas linhas com o uso do “\n”.