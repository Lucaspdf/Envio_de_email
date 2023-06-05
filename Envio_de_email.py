import pyautogui import time

retorno_de_vendas = 100.000

gastos = 60.000

lucratividade = retorno_de_vendas - gastos 
pyautogui.click(x=643, y=1053) 
pyautogui.sleep(5) 
pyautogui.click(x=118, y=121) 
pyautogui.sleep(5) 
pyautogui.write("lucasdanielcuia45@yahool.com") 
pyautogui.click(x=1074, y=361) 
pyautogui.write(f"Ola Lucas esta e a lucratividade obtida R${lucratividade}!") 
pyautogui.sleep(5)
pyautogui.click(x=1802, y=144) 
pyautogui.sleep(5)
pyautogui.click(x=1891, y=22)