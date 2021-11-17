#EJERCICIO CLASE 8
#   desarrollar un modulo python que repita el ejercicio de clase 7 usando json:
    # 1. pide por teclado los datos para una lista en la que cada elemento es un diccionario con keywords "marca coche", "modelo", "combustible" y "cilindrada".
    #   se termina de introducir elementos en la lista cuando el nombre es "fin"
    # 2. vacia la lista
    # 3. lee del archivo "coches.txt" los datos, los almacena de nuevo en la lista y los escribe por pantalla

import json
 = []
lista_coche
while True:
    marcacoche = input("marca coche: ")
    if marcacoche == "fin":
        break
    modelo = input("modelo: ")
    combustible = input("tipo combustible: ")
    cilindrada = input("cilindrada: ")
    linea= {}
    linea["marca coche: "] = marcacoche
    linea["modelo: "] = modelo
    linea["combustible: "] = combustible
    linea["cilindrada: "] = cilindrada
    lista_coche.append(linea)
print("Lista coche:\n", lista_coche)

json.dump(json.dumps(lista_coche), open("coches.txt", "w"))

lista_coches = []
