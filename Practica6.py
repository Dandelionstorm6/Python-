# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 13:56:26 2021

@author: dande
"""

#libreria para llamar al sistema operativo
#usé anaconda y spyder para programar, no tuve que instalar nada solo poner los imports 

import os
import sqlite3

conexion = sqlite3.connect('informacion.db')
c = conexion.cursor()

c.execute("CREATE TABLE registro ('id' integer PRIMARY KEY, 'direccion_ip' text,'activa' boolean) ")
print("Inserta una direccion ip")
hostname = input()
a = 0
puntuacion = '/'
puntuacion2 = '.'
hostname2 = ""
for caracter in hostname:
    if(caracter not in puntuacion2):
        if (a != 3):    
            hostname2 = hostname2 + caracter
        else:
            hostname2 = hostname2
    else:
        hostname2 = hostname2 + caracter
        a+=1
print(hostname2)

if (hostname[-1] != '0'):
    respuesta = os.system("ping " + hostname)
    if respuesta == 0:
        print(hostname + ": está en funcionamiento!")
    else:
        print(hostname + ": No funciona!")
    
    c.execute("INSERT INTO registro (direccion_ip, activa) values (?,?)", (hostname,respuesta))
    conexion.commit()
else:
    for i in range(1,255):
        respuesta = os.system("ping " + hostname2+str(i))
        nuevo = hostname2 +  str(i)
        if respuesta == 0:
            print(nuevo + ": está en funcionamiento!")
        else:
            print(nuevo + ": No funciona!")
        c.execute("INSERT INTO registro (direccion_ip, activa) values (?,?)", (nuevo,respuesta))
        conexion.commit()



    
c.execute('Select * FROM registro')

print('Imprimiendo regitros')
regitros = c.fetchall()
for ciclo in regitros:
    print(ciclo)