#PyAutoGUI: Permite desenvolver aplicações python que controlem o mouse e o teclado para automatizar as interações com outros aplicativos.


#Para fazer a instalação básica, é necessário escrever na linha de comando:

!pip install PyAutoGUI


#Uma forma de testar a instalação é escrever e executar o programa:

import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.click(100, 200)
pyautogui.move(0, 10)
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.write('Olá, Mundo!', interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.alert('Esta é a mensagem para Tela.')



# Nesse código, basicamente tem-se esta sequência de instruções:
# Obter o tamanho do monitor principal.
# Obter a posição XY do mouse.
# Mover o mouse para as coordenadas XY.
# Clicar com o mouse.
# Mover o mouse para as coordenadas XY e clicar nelas.
# Mover o mouse 10 pixels para baixo de sua posição atual.
# Clicar duas vezes com o mouse.
# Usar a função de interpolação/atenuação para mover o mouse por 2 segundos com pausa de um quarto de segundo entre cada tecla.
# Pressionar a tecla Esc.
# Pressionar a tecla Shift e segurá-la.
# Pressionar a tecla de seta para a esquerda 4 vezes.
# Soltar a tecla Shift.
# Pressionar a combinação de teclas de atalho Ctrl-C.
# Mostrar uma caixa de alerta aparecer na tela e pausar o programa até clicar em OK.