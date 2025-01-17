#listas
'''
lista1=[10,5,3]
lsita2=[1.1,2.5,3.99,9.84]
lista3=["hola","mundo","python"]
lista4=["Juan", 45,1.92]

print(type(lista1))
print(len(lista1))

print(lista1[0])


x=0
suma=0
while x<len(lista1):
    suma=suma+lista1[x]
    x+=1

print("la suma es: {}".format(suma)) 


print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)

lista5=[]

for x in range(1):
    valor=int(input("ingresa valor: "))
    lista5.append(valor)

print(lista5)

print(lista1)
lista1.pop()
print(lista1)
'''

valor=int(input("ingresa tamaño lista: "))
lista1=[]

for i in range(valor):
    lista1.append(i)

lista2=[]
x=0
while x<len(lista1):
    lista2.append(lista1[x])
    x=x+2

lista3=[]
y=0
while y<len(lista1):

    if lista1[y]%2!=0:
        lista3.append(lista1[y])
    else:
        pass
        
    y=y+1



print(lista1)
print("Los numeros pares son: ", lista2)
print("Los numeros impares son: ", lista3)

'''
lista1.sort()
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)
'''