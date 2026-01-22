import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://web.whatsapp.com/")
pyautogui.press("enter")

time.sleep(10)

# Clicar na barra de pesquisa (AJUSTE)
x_pesquisa = 316
y_pesquisa = 207
pyautogui.click(x_pesquisa, y_pesquisa)

# Buscar contato
pyautogui.write("Welton")
pyautogui.press("enter")

time.sleep(2)

# Enviar mensagem
pyautogui.write("ALISTAMENTO OBRIGATORIO")
pyautogui.press("enter")

print("Mensagem enviada com sucesso")