print("🔥 VERSÃO NOVA DO ARQUIVO 🔥")

import pyautogui
import time

print("Script iniciado")
print("Você tem 5 segundos para posicionar o mouse no local do clique")

time.sleep(5)

x, y = pyautogui.position()
print(f"Coordenadas capturadas: x={x}, y={y}")

print("Clicando em 3 segundos...")
time.sleep(3)

pyautogui.click(x, y)

print("Clique realizado com sucesso")




