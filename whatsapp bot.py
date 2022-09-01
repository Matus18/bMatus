import pyautogui, webbrowser, time

numero_telefono = '+56981209669'
url = 'https://web.whatsapp.com/send?phone='
webbrowser.open(url+ numero_telefono)
time.sleep(8)
pyautogui.write('mensaje de prueba')
pyautogui.press('enter')
