from bs4 import BeautifulSoup
import requests
import webbrowser
import time

url = requests.get('')# agregar pagina

soup =BeautifulSoup(url.content, "html parser")
resultado = soup.find("span", {}) # agregar tipo de class de la pagina
precioInicial_text = resultado.text
precioInciail = float(precioInicial_text)
precioDeseado = 11.111 #indicar precio que desea

if precioInciail > precioDeseado:
    print("Hay oferta.")
else:
    print("No hay oferta.")
