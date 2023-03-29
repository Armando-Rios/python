import pickle


f = open("archivo.txt", "w")
f.write("Archivo Creado\n")
f.close()

f = open("archivo.txt", "r+")
f.readline()
f.write("Escribiendo otra linea\n")
