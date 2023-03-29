import pickle


class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getAnio(self):
        return self.anio


# Crear un objeto de la clase Vehiculo
mi_auto = Vehiculo("Toyota", "Corolla", 2022)

# Guardar el objeto en un archivo utilizando la biblioteca pickle
with open("mi_auto.pickle", "wb") as archivo:
    pickle.dump(mi_auto, archivo)

# Cargar el objeto desde el archivo
with open("mi_auto.pickle", "rb") as archivo:
    objeto_cargado = pickle.load(archivo)

# Imprimir los atributos del objeto cargado
print("Marca:", objeto_cargado.getMarca())
print("Modelo:", objeto_cargado.getModelo())
print("Año:", objeto_cargado.getAnio())
