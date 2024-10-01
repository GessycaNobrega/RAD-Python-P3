#Kivy: É um framework python de código aberto para o desenvolvimento de aplicações com interfaces de usuário e multitoque. Ele é escrito em python e Cython, baseado em OpenGL ES 2, suporta vários dispositivos de entrada e possui uma extensa biblioteca de componentes (widgets). Com o mesmo código, a aplicação funciona para Windows, macOS, Linux, Android e iOS. Todos os widgets Kivy são construídos com suporte multitoque.

#Para instalá-lo, é necessário escrever na linha de comando:

pip install Kivy

#Uma forma de testar a instalação é escrever e executar o programa:

from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')