# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:30:54 2021

@author: dande
"""

import os
import subprocess
import sqlite3

conexion = sqlite3.connect('informacion.db')
c = conexion.cursor()

direccion_ip = "192.168.0.21"

print("Direccion ip que se va a analizar: " + direccion_ip)
resultado = os.popen("nmap -sT "+direccion_ip).readlines()
puertos = resultado[5:len(resultado)-2]

for lista in puertos:
    campos = lista.split()
    print("ip: "+direccion_ip + " - status: " + campos[1] + " - service: " + campos[2])
    


c.execute('Select * FROM registro')
