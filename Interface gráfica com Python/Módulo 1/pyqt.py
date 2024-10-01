#Trata-se de um framework que aborda, além de desenvolvimento GUI, abstrações de sockets de rede, threads, Unicode, expressões regulares, bancos de dados SQL, OpenGL, XML, entre outras aplicações.

#Para fazer a instalação básica, é necessário escrever na linha de comando:


pip install PyQt5


#Uma forma de testar a instalação é escrever e executar o programa:


import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class HelloWindow(QMainWindow):
   def __init__(self):
      QMainWindow.__init__(self)

      self.setMinimumSize(QSize(280, 120))
      self.setWindowTitle("Olá, Mundo! Exemplo PyQT5")

      centralWidget = QWidget(self)
      self.setCentralWidget(centralWidget)

      gridLayout = QGridLayout(self)
      centralWidget.setLayout(gridLayout)

      title = QLabel("Olá Mundo para PyQt", self)
      title.setAlignment(QtCore.Qt.AlignCenter)
      gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   mainWin = HelloWindow()
   mainWin.show()
   sys.exit( app.exec_() )