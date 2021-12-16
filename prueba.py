# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:24:56 2021

@author: dande
"""
import sqlite3

import tkinter as tk
from tkinter import ttk

conexion = sqlite3.connect('informacion.db')
c = conexion.cursor()
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