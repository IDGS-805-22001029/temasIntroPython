import os

#Para crear funciones en Python se utiliza la palabra reservada def
def function1():
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = input("Primer número: ")
    num2 = input("Segundo número: ")
    res=num1+num2
    print("La suma de {} + {} es{}".format(num1,num2,res))

def function2():
    print("Hola, soy la funcion 2")

def run():
    os.system('cls')
    print("Menú de opciones: ")
    print("1.- la suma de dos números")
    print("2.- Otra función")
    print("3.- Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        function1()
    if opcion == 2:
        function2()

'''
op=int(input("Numero: "))
        if op==1:
            function1()
        else:
            function2()
            '''

if__name__ == "__main__":
    run