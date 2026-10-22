import numpy as np 
# Adrian Hinojos NC:1344
# Ejemplos de numpy numerica python 
print(" --- Espaciado  linealmente en array --- 1344")
arre=np.linspace(start=0,stop=1,num=5)
print(arre)
print("--- Matrix identidad en 2D array --- 1344")
matrix=np.eye(3)
print(matrix)
print("--- Genera numeros al azar(Aleatorios) en 2D array --- 1344")
Numale=np.random.random((3,4)) # genera 12 numeros aleatorios 
print(Numale)
print("Generar 9 Numeros aleatorios entre 0 y 1")
Numale=np.random.random((3,3)) # genera 9 numeros aleatorios 
print(Numale)
# como generar 9 numeros aleatorios  comprendidios entre 1 y  20  
# con numpy en un arreglo de 3 por 3
print("Generar 9 Numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Adrian Hinojos NC 1344")
