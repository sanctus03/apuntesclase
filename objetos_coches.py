import persistencia_pickle as pp
import car_class
import random as rd
FILE = "coches.obj.txt"

lista_coches = pp.retrieve(FILE)
if lista_coches == none:
    lista_coches = []
while True:
    marca = input("marca: ")
    if marca == 'fin':
        break
    modelo = input("modelo: ")
    combustible = input("combustible: ")
    cilindrada = input("cilindrada: ")
    coche = car_class.car(marca, modelo, combustible, cilindrada)
    lista_coches.append(coche)

    coche.move_pos((rd.random), *100, rd.random()*600)

    print("posición: ", coche.get_pos())
    coche.move_incr(rd.random()*10, rd.random()*60)
    print("Posición: ", coche.get_pos())
    del(coche)
pp.store(lista_coches, FILE)
lista_coches = []
lista_coches = pp.load(FILE)
for car in lista_coches:
    print("marca, modelo, combustible, cilindrada", car.marca, car.modelo, car.combustible, car.cilindrada)
    print("posición", car.get_pos(), '\n')
