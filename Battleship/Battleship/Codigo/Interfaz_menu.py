from tkinter import * 
from PIL import ImageTk, Image
import tkinter as tk
import logica as log
import generic as gen
from tkinter import messagebox
from Interfaz_juego import *


def enter(event):
    """Ejecuta la tecla enter

    Args:
        evet (_type_): Tecla enter
    """
    log.almacenar_nombre(nombre_jugador, indicacion, abrir_menu)

def abrir_menu_principal():
    """Cierra el frame del menú añadir jugadores y muestra el frame del menú principal.
    """
    frame_añadir_jugadores.pack_forget()
    frame_principal.pack()
    
def abrir_menu_añadir_jugadores():
    """Cierra el frame del menú principal y muestra el frame del menú principal 
    """
    frame_principal.pack_forget()
    frame_añadir_jugadores.pack(expand= tk.TRUE, fill=tk.BOTH)
    
def abrir_menu_tablero():
    """Cierra el frame del menú principal y muestra el frame del menú donde se define las dimensiones del tablero si, solo si se han agregado los dos jugadores.
    """
    if len(log.jugador1) and len(log.jugador2) > 0:
        frame_principal.pack_forget()
        frame_dimensiones.pack(side=tk.LEFT, expand= tk.TRUE, fill=tk.BOTH)
        frame_agua.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
    else:
        messagebox.showerror(message="Deja la vagancia, agrega esos jugadores.", title="Mensaje")

def abrir_colocar_jugador1():
    """Cierra el frame del menú y muestra el frame del menú donde se colocan los barcos del jugador 1.
    """
    frame_dimensiones.pack_forget()
    frame_agua.pack_forget()
    frame_jugador.pack(side=tk.LEFT, expand= tk.TRUE, fill=tk.BOTH)
    tablero.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

def abrir_colocar_jugador2():
    """Cierra el frame del menú donde se colocan los barcos del jugador 1 y muestra el frame del menú donde se colocan los barcos del jugador 2.
    """
    if mat. contador_destructor == 6 and mat.contador_crucero == 4  and mat.contador_acorazado == 2:
        frame_jugador.pack_forget()
        tablero.pack_forget()
        frame_jugador2.pack(side=tk.LEFT, expand= tk.TRUE, fill=tk.BOTH)
        tablero2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
    else:  messagebox.showerror(message="No hagas trampa, coloca todos tus barcos", title="Mensaje")

def abrir_juego(m_1,m_2,j_1,j_2,v):
    """Cierra el frame del menú donde se colocan los barcos del jugador 1 y llama a la función 'interfaz juego'

    Args:
        m_1 (_type_): Matriz del jugador 1.
        m_2 (_type_): Matriz del jugador 2.
        j_1 (_type_): Lista donde se almacena el jugador 1.
        j_2 (_type_): Lista donde se almacena el jugador 2.
        v (_type_): Ventana de la aplicación.
    """
    if mat. contador_destructor == 6 and mat.contador_crucero == 4  and mat.contador_acorazado == 2:
        frame_jugador2.pack_forget()
        tablero2.pack_forget()
        interfaz_juego(matriz_jugador_1=m_1,matriz_jugador_2=m_2,ventana=v,jugador_1=j_1,jugador_2=j_2)
    else:  messagebox.showerror(message="No hagas trampa, coloca todos tus barcos", title="Mensaje")

def label_config(label, jugador):
    label.config(text=f"{jugador[0]}")


#Ventana principal
ventana = tk.Tk()
ventana.title("BattleShip")
ventana.geometry("800x600")
ventana.resizable(False, False)
vcmd = gen.call(ventana)
gen.centrar_ventana(ventana, 800,600)
import matrices as mat


# Frame para el menú principal
frame_principal = tk.Frame(ventana)
# Fondo de la ventana principal
imagen = Image.open("imagenes/fondo/fondo2.png")
imagen_redimensionada = imagen.resize((800, 600))
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
fondo = tk.Label(frame_principal, image=imagen_tk)
fondo.pack(fill=BOTH, expand=TRUE)
# Boton para iniciar juego (en el menú principal)
boton_iniciar = Button(frame_principal, text="Iniciar juego", bg="white", fg='#1ca0eb',relief=FLAT, font=("Impact",11), command=abrir_menu_tablero)
boton_iniciar.place(relx=0.5, rely=0.8, relwidth=0.15, relheight=0.051, anchor=CENTER)
# Boton para añadir jugadores
boton_menu_añadir_jugadores = tk.Button(frame_principal, text="Añadir Jugadores",fg='#1ca0eb',relief=FLAT, font=("Impact",11),bg="white", command=abrir_menu_añadir_jugadores)
boton_menu_añadir_jugadores.place(relx=0.5, rely=0.9, relwidth=0.15, relheight=0.051, anchor=CENTER)


# Frame para el menú de añadir jugadores
frame_añadir_jugadores = tk.Frame(ventana, bd=0, relief=tk.FLAT, bg="#46eb72")
label_titulo= tk.Label(frame_añadir_jugadores, text="BattleShip", bg='#46eb72', fg='#ffffff',font=("Impact", 40))
label_titulo.place(x=0,y=0,relwidth=1,relheight=0.3)
# Indicación
indicacion = tk.Label(frame_añadir_jugadores, text="Añade el jugador 1", bg='#46eb72', fg='#ffffff',font=("Impact", 20))
indicacion.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.3, anchor=CENTER)
# Entrada nombre jugadores
nombre_jugador = tk.Entry(frame_añadir_jugadores,  width=20, relief= "flat", font=("Cambria", 14, "bold"), 
                       justify="center", bg='#ffffff', fg='#46eb72')
nombre_jugador.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.05, anchor=CENTER)
nombre_jugador.bind("<Return>", enter)
# Boton añadir jugador
boton_añadir_jugador = tk.Button(frame_añadir_jugadores, text="Añadir jugador", bd=0, font=("Impact", 16), 
                                justify="center", bg='#ffffff', fg='#46eb72', relief=tk.FLAT,
                                command=lambda: log.almacenar_nombre(nombre_jugador, indicacion, 
                                                                    abrir_menu))
boton_añadir_jugador.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.05, anchor=CENTER)


#frame dimensiones
frame_dimensiones= tk.Frame(ventana, bd=0, width=200, relief=tk.GROOVE, padx=10, pady=10, bg='#46eb72')
#Label nombre juego
label_nombre= tk.Label(frame_dimensiones, text="BattleShip", bg='#46eb72', fg='#ffffff',font=("Impact", 24))
label_nombre.place(x=0,y=50,relwidth=1,relheight=0.07)
#Label instruccion
label_instrucción_tablero= tk.Label(frame_dimensiones, text="Elige el tamaño del tablero:", bg='#46eb72', 
                                    fg='#ffffff', font=("Cambria ", 10,"bold"))
label_instrucción_tablero.place(x=0,y=175,relwidth=1,relheight=0.05)
#Instruccion Fila
label_fila= tk.Label(frame_dimensiones, text="Filas:", bg='#46eb72', fg='#ffffff', font=("Impact", 12))
label_fila.place(x=30,y=225,relwidth=0.2,relheight=0.04)
#Entrada Fila
entry_fila = tk.Entry (frame_dimensiones,  width=20, relief= "flat", font=("Cambria", 11, "bold"), 
                       justify="center", bg='#ffffff', fg='#46eb72', validate="key", 
                       validatecommand=(vcmd, "%P"))
entry_fila.place(x=85,y=225,relwidth=0.4,relheight=0.04)
#Instruccion columna
label_columna= tk.Label(frame_dimensiones, text="Columnas:", bg='#46eb72', fg='#ffffff', font=("Impact",12))
label_columna.place(x=11,y=275,relwidth=0.4,relheight=0.04)
#Entrada columna
entry_columna = tk.Entry (frame_dimensiones,  width=20, relief="flat", font=("Cambria", 11, "bold"), 
                          justify="center", bg='#ffffff', fg='#46eb72', validate="key", 
                          validatecommand=(vcmd, "%P"))
entry_columna.place(x=85,y=275,relwidth=0.4,relheight=0.04)
#Boton crear tablero
boton_tablero = tk.Button(frame_dimensiones, text="Crear tablero", bd=0, font=("Impact", 11), 
                          justify="center", bg='#ffffff', fg='#46eb72', relief=tk.FLAT,
                          command=lambda:[mat.crear_matrices(entry_fila, entry_columna), mat.crear_botones(mat.matriz1, tablero), label_config(label_jugador, log.jugador1), abrir_colocar_jugador1()])
boton_tablero.place(x=0,y=375,relwidth=1,relheight=0.07)


#Frame agua
frame_agua = tk.Frame(ventana, width=600, relief=tk.SOLID, bg='#7efca0')
#Fondo agua
imagen2 = Image.open("Imagenes/más/agua.jpg")
imagen_redimensionada2 = imagen2.resize((600, 600))
imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada2)
label_agua= tk.Label(frame_agua, image=imagen_tk2)
label_agua.pack(fill=tk.BOTH, expand=tk.TRUE)


#Frame jugador
frame_jugador = tk.Frame(ventana, width=200, relief=tk.SOLID, bg='#1ca0eb', padx=10,pady=10)
label_jugador= tk.Label(frame_jugador, text=log.jugador1, bg='#1ca0eb', fg='#ffffff',font=("Comic Sans MS", 24, "bold"))
label_jugador.place(x=0,y=40,relwidth=1,relheight=0.07)
label_instrucción_jugador= tk.Label(frame_jugador, text="Coloca tus barcos", bg='#1ca0eb',
                                    fg='#ffffff', font=("Cambria", 11,"bold"))
label_instrucción_jugador.place(x=0,y=90,relwidth=1,relheight=0.2)
#Flecha izquierda
flecha_west_original = Image.open("imagenes/más/flecha.png")
flecha_west_redimensionado = flecha_west_original.resize((15, 15))
flecha_west = ImageTk.PhotoImage(flecha_west_redimensionado)
west_button = tk.Button(frame_jugador, image=flecha_west, command=lambda: mat.brujula(1))
west_button.place(x=47,y=200,relwidth=0.15,relheight=0.05)
#Flecha arriba
flecha_north_original = Image.open("imagenes/más/flecha.png")
north_rotate = flecha_north_original.rotate(270)
flecha_north_redimensionado = north_rotate.resize((15, 15))
flecha_north = ImageTk.PhotoImage(flecha_north_redimensionado)
north_button = tk.Button(frame_jugador, image=flecha_north, command=lambda: mat.brujula(2))
north_button.place(x=82,y=170,relwidth=0.15,relheight=0.05)
#Flecha abajo
flecha_south_original = Image.open("imagenes/más/flecha.png")
south_rotate = flecha_south_original.rotate(90)
flecha_south_redimensionado = south_rotate.resize((15, 15))
flecha_south = ImageTk.PhotoImage(flecha_south_redimensionado)
south_button = tk.Button(frame_jugador, image=flecha_south, command=lambda: mat.brujula(3))
south_button.place(x=82,y=230,relwidth=0.15,relheight=0.05)
#Flecha derecha
flecha_east_original = Image.open("imagenes/más/flecha.png")
east_rotate = flecha_east_original.rotate(180)
flecha_east_redimensionado = east_rotate.resize((15, 15))
flecha_east = ImageTk.PhotoImage(flecha_east_redimensionado)
east_button = tk.Button(frame_jugador, image=flecha_east, command=lambda: mat.brujula(0))
east_button.place(x=117,y=200,relwidth=0.15,relheight=0.05)
#Boton destructor
original_destructor = Image.open("imagenes/barcos/b1.png")
destructor_redimensionada = original_destructor.resize((55, 55))
imagen_destructor = ImageTk.PhotoImage(destructor_redimensionada)
boton_destructor = tk.Button(frame_jugador, image=imagen_destructor, 
                             command=lambda:mat.barco_seleccionado(1,0,0), relief="ridge",bd=4)
boton_destructor.place(x=62, y=280, relwidth=0.4, relheight=0.1)
#Boton crucero
original_crucero1 = Image.open("imagenes/barcos/b22.png")
original_crucero2 = Image.open("imagenes/barcos/b21.png")
ancho_crucero1, alto_crucero1 = original_crucero1.size
resized_crucero2 = original_crucero2.resize((ancho_crucero1, alto_crucero1))
crucero_combinada = Image.new("RGBA", (ancho_crucero1 * 2, alto_crucero1))
crucero_combinada.paste(original_crucero1, (0, 0))
crucero_combinada.paste(resized_crucero2, (ancho_crucero1, 0))
crucero_redimensionada = crucero_combinada.resize((55, 55))
imagen_crucero = ImageTk.PhotoImage(crucero_redimensionada)
boton_crucero = tk.Button(frame_jugador, image=imagen_crucero, command=lambda: mat.barco_seleccionado(2,3,0), 
                          relief="ridge", bd=4)
boton_crucero.place(x=62, y=345, relwidth=0.4, relheight=0.1)
#Botón acorazado
original_acorazado1 = Image.open("imagenes/barcos/b33.png")
original_acorazado2 = Image.open("imagenes/barcos/b32.png")
original_acorazado3 = Image.open("imagenes/barcos/b31.png")
ancho_acorazado1, alto_acorazado1 = original_acorazado1.size
resized_acorazado2 = original_acorazado2.resize((ancho_acorazado1, alto_acorazado1))
resized_acorazado3 = original_acorazado3.resize((ancho_acorazado1, alto_acorazado1))
imagen_combinada = Image.new("RGBA", (ancho_acorazado1 * 3, alto_acorazado1))
imagen_combinada.paste(original_acorazado1, (0, 0))
imagen_combinada.paste(resized_acorazado2, (ancho_acorazado1, 0))
imagen_combinada.paste(resized_acorazado3, (ancho_acorazado1 * 2, 0))
acorazado_redimensionada = imagen_combinada.resize((55, 55))
imagen_acorazado = ImageTk.PhotoImage(acorazado_redimensionada)
boton_acorazado = tk.Button(frame_jugador, image=imagen_acorazado, command=lambda: mat.barco_seleccionado(4,5,6),
                            relief="ridge", bd=4)
boton_acorazado.place(x=62, y=410, relwidth=0.4, relheight=0.1)
#Boton listo
boton_listo = tk.Button(frame_jugador, text="Listo", bd=0, font=("Impact", 11), 
                          justify="center", bg='#ffffff', fg='#1ca0eb', relief=tk.FLAT,
                          command=lambda:[abrir_colocar_jugador2(), mat.crear_botones(mat.matriz2, tablero2),  label_config(label_jugador2, log.jugador2)])
boton_listo.place(x=32, y=490, relwidth=0.7, relheight=0.07)

#Frame tablero 1
tablero = tk.Frame(ventana, width=600, relief=tk.SOLID)


#Frame jugador 2
frame_jugador2 = tk.Frame(ventana, width=200, relief=tk.SOLID, bg='#9e2020',)
label_jugador2= tk.Label(frame_jugador2, text=log.jugador2, bg='#9e2020', fg='#ffffff',font=("Comic Sans MS", 24, "bold"))
label_jugador2.place(x=0,y=40,relwidth=1,relheight=0.07)
label_instrucción_jugador2= tk.Label(frame_jugador2, text="Coloca tus barcos", bg='#9e2020',
                                    fg='#ffffff', font=("Cambria", 11,"bold"))
label_instrucción_jugador2.place(x=0,y=90,relwidth=1,relheight=0.2)
#Flecha izquierda 2
flecha_west_original2 = Image.open("imagenes/más/flecha.png")
flecha_west_redimensionado2 = flecha_west_original2.resize((15, 15))
flecha_west2 = ImageTk.PhotoImage(flecha_west_redimensionado2)
west_button2 = tk.Button(frame_jugador2, image=flecha_west2, command=lambda: mat.brujula(1))
west_button2.place(x=47,y=200,relwidth=0.15,relheight=0.05)
#Flecha arriba 2
flecha_north_original2 = Image.open("imagenes/más/flecha.png")
north_rotate2 = flecha_north_original2.rotate(270)
flecha_north_redimensionado2 = north_rotate2.resize((15, 15))
flecha_north2 = ImageTk.PhotoImage(flecha_north_redimensionado2)
north_button2 = tk.Button(frame_jugador2, image=flecha_north2, command=lambda: mat.brujula(2))
north_button2.place(x=82,y=170,relwidth=0.15,relheight=0.05)
#Flecha abajo 2
flecha_south_original2 = Image.open("imagenes/más/flecha.png")
south_rotate2 = flecha_south_original2.rotate(90)
flecha_south_redimensionado2 = south_rotate2.resize((15, 15))
flecha_south2 = ImageTk.PhotoImage(flecha_south_redimensionado2)
south_button2 = tk.Button(frame_jugador2, image=flecha_south2, command=lambda: mat.brujula(3))
south_button2.place(x=82,y=230,relwidth=0.15,relheight=0.05)
#Flecha derecha 2
flecha_east_original2 = Image.open("imagenes/más/flecha.png")
east_rotate2 = flecha_east_original2.rotate(180)
flecha_east_redimensionado2 = east_rotate2.resize((15, 15))
flecha_east2 = ImageTk.PhotoImage(flecha_east_redimensionado2)
east_button2 = tk.Button(frame_jugador2, image=flecha_east2, command=lambda: mat.brujula(0))
east_button2.place(x=117,y=200,relwidth=0.15,relheight=0.05)
#Botón destructor 2
original_destructor_2 = Image.open("imagenes/barcos/b1.png")
destructor_redimensionada_2 = original_destructor_2.resize((55, 55))
imagen_destructor_2 = ImageTk.PhotoImage(destructor_redimensionada_2)
boton_destructor_2 = tk.Button(frame_jugador2, image=imagen_destructor_2, 
                             command=lambda:mat.barco_seleccionado(1,0,0), relief="ridge",bd=4)
boton_destructor_2.place(x=62,y=280,relwidth=0.4,relheight=0.1)
#Botón crucero 2
original_crucero1_2 = Image.open("imagenes/barcos/b22.png")
original_crucero2_2 = Image.open("imagenes/barcos/b21.png")
ancho_crucero1_2, alto_crucero1_2 = original_crucero1_2.size
resized_crucero2_2 = original_crucero2_2.resize((ancho_crucero1_2, alto_crucero1_2))
crucero_combinada_2 = Image.new("RGBA", (ancho_crucero1_2 * 2, alto_crucero1_2))
crucero_combinada_2.paste(original_crucero1_2, (0, 0))
crucero_combinada_2.paste(resized_crucero2_2, (ancho_crucero1_2, 0))
crucero_redimensionada_2 = crucero_combinada_2.resize((55, 55))
imagen_crucero_2 = ImageTk.PhotoImage(crucero_redimensionada_2)
boton_crucero_2 = tk.Button(frame_jugador2, image=imagen_crucero_2, command=lambda: mat.barco_seleccionado(2,3,0), 
                          relief="ridge", bd=4)
boton_crucero_2.place(x=62,y=345,relwidth=0.4,relheight=0.1)
#Botón acorazado 2
original_acorazado1_2 = Image.open("imagenes/barcos/b33.png")
original_acorazado2_2 = Image.open("imagenes/barcos/b32.png")
original_acorazado3_2 = Image.open("imagenes/barcos/b31.png")
ancho_acorazado1_2, alto_acorazado1_2 = original_acorazado1_2.size
resized_acorazado2_2 = original_acorazado2_2.resize((ancho_acorazado1_2, alto_acorazado1_2))
resized_acorazado3_2 = original_acorazado3_2.resize((ancho_acorazado1_2, alto_acorazado1_2))
imagen_combinada_2 = Image.new("RGBA", (ancho_acorazado1_2 * 3, alto_acorazado1_2))
imagen_combinada_2.paste(original_acorazado1_2, (0, 0))
imagen_combinada_2.paste(resized_acorazado2_2, (ancho_acorazado1_2, 0))
imagen_combinada_2.paste(resized_acorazado3_2, (ancho_acorazado1_2 * 2, 0))
acorazado_redimensionada_2 = imagen_combinada_2.resize((55, 55))
imagen_acorazado_2 = ImageTk.PhotoImage(acorazado_redimensionada_2)
boton_acorazado_2 = tk.Button(frame_jugador2, image=imagen_acorazado_2, command=lambda: mat.barco_seleccionado(4,5,6),
                            relief="ridge", bd=4)
boton_acorazado_2.place(x=62,y=410,relwidth=0.4,relheight=0.1)
#Botón listo 2
boton_listo2 = tk.Button(frame_jugador2, text="Listo", bd=0, font=("Impact", 11), 
                          justify="center", bg='#ffffff', fg='#9e2020', relief=tk.FLAT,
                          command=lambda m_1=mat.matriz1,m_2=mat.matriz2,ju_1=log.jugador1,ju_2=log.jugador2,ven=ventana: abrir_juego(m_1=m_1,m_2=m_2,j_1=ju_1,j_2=ju_2,v=ven))
boton_listo2.place(x=32,y=490,relwidth=0.7,relheight=0.07)

#Frame tablero 2
tablero2 = tk.Frame(ventana, width=600, relief=tk.SOLID)

# Mostrar menú principal por defecto
abrir_menu_principal()

abrir_menu = abrir_menu_principal

ventana.mainloop()
