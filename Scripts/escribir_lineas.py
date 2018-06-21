# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:21:40 2018

@author: igarciag
"""
import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Escribe los argumentos correctamente")
    print('Ejemplo: escribir_lineas.py "Texto" 5')