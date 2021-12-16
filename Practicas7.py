# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 01:15:35 2021

@author: dande
"""

import sqlite3
import os
import tkinter as tk
from tkinter import ttk

conexion = sqlite3.connect('informacion.db')
c = conexion.cursor()

#c.execute("CREATE TABLE servicio ('id' integer PRIMARY KEY, 'Host' text,'Servicio' text, 'Status' text) ")


c.execute('Select * FROM registro')

regitros = c.fetchall()
for ciclo in regitros:
    if(ciclo[2] == 0):
        resultado = os.popen("nmap -sT "+ciclo[1]).readlines()
        puertos = resultado[5:len(resultado)-2]
        for lista in puertos:
            campos = lista.split()
            c.execute("INSERT INTO servicio (Host, Servicio,Status) values (?,?,?)", (ciclo[1],campos[1],campos[2]))
            conexion.commit()
            
c.execute('Select * FROM servicio')


ventana = tk.Tk()
ventana.title("Regitro servicios")

regitros = c.fetchall()
a=0
b=0
for ciclo in regitros:
    ttk.Label(ventana, text=str(ciclo[1])+"  "+str(ciclo[2])+"  "+str(ciclo[3])).grid(column=a,row=b)
    b+=1
    if(b>8):
        a+=1
        b=0
    
   


ventana.mainloop()        