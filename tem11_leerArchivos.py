from io import open

fichero = open('fichero.pdf', 'r')
texto1 = fichero.readlines()
print(texto1)
print(type(texto1))
fichero.close()

for i in texto1:
    print(i)

for i in texto1:
    for e in i:
        print(e)
