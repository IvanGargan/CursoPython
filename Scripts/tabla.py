# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:16:01 2018

@author: igarciag
"""

import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    
    if filas < 1 or filas > 9 or columnas <1 or columnas > 9:
        print("Los números a introducir tienen que estar entre 1 y 9")
        print('Ejemplo: tabla.py 7 3')
    else:
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end='')

else:
    print("Escribe los argumentos correctamente")
    print('Ejemplo: tabla.py 7 9')
