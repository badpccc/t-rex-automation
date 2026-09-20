import pyautogui
import time

time.sleep(3)

while True:

    x, y = pyautogui.position()

    cor_fundo = pyautogui.pixel(x, y)

    print(f'Detector: ({x}, {y})')
    print(f'Background Color: {cor_fundo}')

    cor_atual = pyautogui.pixel(x, y)

    if cor_atual != cor_fundo:
        pyautogui.press('space')
        time.sleep(0.3)