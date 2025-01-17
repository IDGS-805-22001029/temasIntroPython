#calcular la distancia entre dos puntos (coordenadas)

import math


'''
#?Para meter las coordenadas de los puntos, se debe de meter de la siguiente manera:
#!ej: 22
#?El código separa automaticamente los valores con una coma
'''


print("Ingresa las coordenadas de dos puntos para calcular la distancia entre ellos")
coo1=[]
coo2=[]

uno=input("Introduzca las coordenadas del primer punto (x1,y1): ")
uno.split(",")
coo1.append(int(uno[0]))
coo1.append(int(uno[1]))

dos=input("Introduzca las coordenadas del segundo punto (x2,y2): ")
dos.split(",")
coo2.append(int(dos[0]))
coo2.append(int(dos[1]))


d = math.sqrt((coo2[0]-coo1[0])**2 + (coo2[1]-coo1[1])**2)

print("La distancia entre los dos puntos es: ", d)