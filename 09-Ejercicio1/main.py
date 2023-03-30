# Pedimos al usuario que ingrese la lista de países separados por comas
paises_input = input("Ingrese una lista de países separados por comas: ")

# Separamos los países y eliminamos espacios extra
paises = [pais.strip() for pais in paises_input.split(",")]

# Convertimos la lista en un conjunto para eliminar duplicados y volvemos a convertirlo en una lista
paises = list(set(paises))

# Ordenamos la lista alfabéticamente
paises.sort()

# Imprimimos la lista de países
print("Países:", ", ".join(paises))
