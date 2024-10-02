#O código para gerar uma aplicação com esse componente é dado por:

import tkinter as tk
janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).pack()
tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)
janela.mainloop()



#Linha 4 - É instanciado um componente “label” com a parametrização das propriedades “text”, “justify” e “padx” que correspondem, respectivamente, ao texto, a como ele será justificado e à largura em pixels do componente.
#Linha 5 e 6 - São instanciados os componentes “radiobuttons”. A propriedade “variable” recebe o valor “v”, indicando que o componente será colocado na vertical.