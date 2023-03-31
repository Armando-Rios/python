from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def suma_impares(lista):
    # Obtener los elementos impares de la lista
    impares = filter(lambda x: x % 2 != 0, lista)
    # Sumar los elementos impares usando reduce
    suma = reduce(lambda x, y: x + y, impares)
    return suma


print(suma_impares(lista))  # Devuelve 25
