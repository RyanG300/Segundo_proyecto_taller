from tkinter import*
import tkinter as tk
from tkinter import messagebox

jugador1 = []
jugador2 = []
contador_jugadores = 1

def almacenar_nombre(nombre_jugador, indicacion, abrir_menu):
    """Almacena los nombres de los jugadores en una lista y agrega otra lista para almacenar el puntaje.

    Args:
        nombre_jugador (_type_): Entrada para agregar el nombre de cada jugador.
        indicacion (_type_): Idiciación para el usuario
        abrir_menu (_type_): Menú para añadir jugadores
    """
    global contador_jugadores
    if contador_jugadores == 1:
        if nombre_jugador.get() == "":
            nombre_jugador.delete(0, tk.END)
            nombre_jugador.focus() 
            messagebox.showerror(message="Tú nombre es inválido", title="Mensaje")
        else:
            jugador1.append(nombre_jugador.get())
            nombre_jugador.delete(0, tk.END)
            nombre_jugador.focus()
            indicacion.config(text="Añade el jugador 2")
            contador_jugadores += 1
            print(jugador1)
    elif contador_jugadores == 2:
        if nombre_jugador.get() == jugador1[0]:
            nombre_jugador.delete(0, tk.END)
            nombre_jugador.focus() 
            messagebox.showerror(message="Sé creativo, no copies, introduce otro nombre", title="Mensaje")
        elif nombre_jugador.get() == "":
                nombre_jugador.delete(0, tk.END)
                nombre_jugador.focus() 
                messagebox.showerror(message="Tú nombre es inválido", title="Mensaje")
        else:
            jugador2.append(nombre_jugador.get())
            nombre_jugador.delete(0, tk.END)
            nombre_jugador.focus() 
            contador_jugadores+=1
            print(jugador2)
            abrir_menu()
    else:
        messagebox.showerror(message="Deja la vagancia, vamos agrega los jugadores", title="Mensaje")
        abrir_menu()

