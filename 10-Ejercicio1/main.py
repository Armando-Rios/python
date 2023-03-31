import tkinter as tk

# Crear la ventana
window = tk.Tk()
window.title('Lista de opciones')

# Definir la lista de opciones
opciones = ['Opción 1', 'Opción 2', 'Opción 3']

# Definir la variable de control para la selección de opciones
seleccion = tk.StringVar()

# Función para mostrar la opción seleccionada


def mostrar_seleccion():
    if seleccion.get():
        seleccionada = seleccion.get()
        mensaje.config(text='Opción seleccionada: ' + seleccionada)

# Función para reiniciar la selección de opciones


def reiniciar_seleccion():
    seleccion.set('')
    mensaje.config(text='')


# Crear los RadioButton y agregarlos a la ventana
for opcion in opciones:
    radio_button = tk.Radiobutton(
        window, text=opcion, variable=seleccion, value=opcion)
    radio_button.pack(anchor='w')

# Crear el botón para mostrar la opción seleccionada
mostrar_button = tk.Button(
    window, text='Mostrar selección', command=mostrar_seleccion)
mostrar_button.pack()

# Crear el botón para reiniciar la selección de opciones
reiniciar_button = tk.Button(
    window, text='Reiniciar selección', command=reiniciar_seleccion)
reiniciar_button.pack()

# Crear la etiqueta para mostrar la opción seleccionada
mensaje = tk.Label(window, text='')
mensaje.pack()

# Mostrar la ventana
window.mainloop()
