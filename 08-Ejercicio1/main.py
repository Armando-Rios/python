import pickle


class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre


f = open("datos.bin", "rb")
auto = pickle.load(f)
f.close()

print(type(auto))
print(auto.getNombre())
