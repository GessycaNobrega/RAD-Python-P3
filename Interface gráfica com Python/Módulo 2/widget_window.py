#O código dessa aplicação é:


import tkinter as tk
janela = tk.Tk()
janela.title(" Aplicação GUI")
janela.mainloop()


#Para fixar o tamanho da janela, é necessário determinar essa propriedade conforme o código seguinte:

import tkinter as tk
janela = tk.Tk()
janela.title(" Aplicação GUI NÃO Dimensionável") 
janela.resizable(False, False)
janela.mainloop()