from io import open 

texto="Una línea con texto\n Otra línea con texto"

fichero=open('fichero.pdf', 'w')
fichero.write(texto)

cadena2="\nEsto es otra cadena de texto"
fichero.write(cadena2)
fichero.close()