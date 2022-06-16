#Antes de rodar utilize o comando: pip install pyautogui

import pyautogui
import time

pyautogui.alert('Para o devido funcionamento do programa, depois de clicar em OK, não mova o mouse ou use o teclado!')
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')

#Escolha o navegador a ser usado - Por padrão foi escolhido o Chrome:
pyautogui.write('Google Chrome')
pyautogui.press('enter')
time.sleep(1)

#Defina dentro das aspas abaixo o link para o Google Drive que será usado - Você já deverá estar logado para que tudo funcione:
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

pyautogui.press('winleft')

#Defina dentro das aspas o nome da pasta onde os arquivos colocados serão enviados para o Drive - Como sujestão dei o nome de 'DriveUp' - Mude de acordo com o nome da sua pasta previamente criada.
file_up = 'DriveUp'
#Faça o mesmo com a pasta em que os arquivos já upados serão colocados - Como sujestão dei o nome de 'DriveUped'
file_uped = 'DriveUped'

pyautogui.write(file_up)
pyautogui.press('enter')

pyautogui.press('f11')
pyautogui.hotkey('ctrl','a')

"""
Importante: A partir desse momento as coordenadas do mouse, necessárias para o devido funcionamento do programa, 
se diferenciam em função do tamanho e resolução do monitor usado.
Portanto é de grande importância que os valores sejam trocados.

Neste site é possível verificar a coordenada do mouse em determinados pontos da tela: http://www.brenz.net/snippets/xy.asp
"""

#Coordenadas para um monitor 1920 x 1080 - Caso o seu seja diferente, troque-as:

#A primeira coordenada usada é do local na tela onde fica o primeiro arquivo de uma pasta com f11 ativo.
pyautogui.moveTo(300, 55)
pyautogui.mouseDown()
#A segunda é na área da tela do Google Drive onde pode-se soltar os arquivos que seram upados.
pyautogui.moveTo(900, 600)

pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.mouseUp()

pyautogui.press('winleft')
pyautogui.write(file_up)
pyautogui.press('enter')
pyautogui.press('f11')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','x')

pyautogui.press('winleft')
pyautogui.write(file_uped)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','v')

pyautogui.alert(f'Os arquivos da pasta {file_up} foram salvos no Google Drive com sucesso!\nOs arquivos já salvos foram redirecionados para a pasta {file_uped}.')