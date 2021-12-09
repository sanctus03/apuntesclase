#   desarrollar un modulo python que pida datos de tipo int por el teclado hasta que se introduzca el numero -9999.
#   controlar que el tipo de dato introducido es correcto mediante try,  except. almacenar los datos en una lista
#   desarrollar un algoritmo que ordene la lista por el metodo de la burbuja
#   escribir el resultado por pantalla

lista = []
while True:
    while True:
        try:
            e = int(input("introduce elementos de lista a ordenar: "))
            break
        except:
            print("el dato introducido no es un numero")
    if(e == -9999):
        break
    lista.append(e)
    n= len(lista)
print("lista sin ordenar \n", lista)
for i in range (n-1):
    for j in range (n-1-i):
        if lista[j] > lista[j+1]:
            aux = lista[j+1]
            lista[j+1] = lista[j]
            lista[j] = aux
print("lista ordenada\n", lista)
