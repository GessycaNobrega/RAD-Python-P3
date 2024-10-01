#É um kit de ferramentas para o desenvolvimento de interfaces gráficas com o usuário implementado em python que faz uso de tecnologia web para sua renderização. O Flexx pode ser usado para criar tanto aplicações de desktop como para web e até mesmo exportar uma aplicação para um documento HTML independente.


#Para instalar o Flexx, basta digitar o comando:

pip install flexx

#No caso do Spyder, o comando deve ser:

!pip install flexx

#Uma forma prática de testar a instalação e aprender um pouco mais sobre esse framework é escrever o código abaixo na linha de comando, ou em um arquivo, e executar:

from flexx import flx
class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()
