import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

matriz1 = []  # Matriz 1
matriz2 = []  # Matriz 2
contador_destructor= 6
contador_crucero= 4
contador_acorazado= 2

def crear_matrices(filas, columnas):
    """Función que crea las matrices según lo indicado por el usuario.

    Args:
        filas (_type_): Filas indicadas por el usuario
        columnas (_type_): Columnas indicadas por el usuario
    """
    i = filas.get()
    j = columnas.get()
    i = int(i)
    j = int(j)
    if i >= 10 and j >= 20:
        j = j // 2
        contador = 0
        for x in range(i):
            matriz1.append([0] * j)
            matriz2.append([0] * j)
            contador += 1
        print(matriz1)
    else:
        messagebox.showerror(message="El tablero debe tener como mínimo 10 filas y 20 columnas.", title="Mensaje")


def crear_botones(matriz, ventana):
    """Crea los botones del tablero y los almacena en una lista

    Args:
        matriz (_type_): Matriz del jugador
        ventana (_type_): Ventana de la aplicación
    """
    global alto_boton, ancho_boton, botones, contador_destructor, contador_acorazado, contador_crucero
    if contador_destructor == 6 and contador_crucero == 4  and contador_acorazado == 2:
        botones = []
        alto_matriz, ancho_matriz = len(matriz), len(matriz[0])
        alto_boton = 600 // alto_matriz
        ancho_boton = 600 // (ancho_matriz-1)

        for i in range(alto_matriz):
            fila=[]
            for j in range(ancho_matriz):
                x = j * ancho_boton
                y = i * alto_boton
                boton = tk.Button(ventana, bd=0, relief=tk.FLAT, image=agua_tk, width=ancho_boton, height=alto_boton, 
                                  command=lambda i=i, j=j: colocar_barcos(i,j, matriz))
                boton.place(x=x, y=y)
                fila.append(boton)
            botones.append(fila)
        contador_destructor, contador_acorazado, contador_crucero = 0, 0, 0


def brujula(num):
    """Recibe la direción como un número, 0: derecha, 1: izquierda, 2: arriba, 3: abajo.

    Args:
        num (_type_): Número de la dirección.
    """
    global direccion_barco
    direccion_barco= num

def barco_seleccionado(indice1,indice2,indice3):
    """Recibe los indices para encontrar las imágenes en el diccionario según el tipo de barco y las agrega a una lista.

    Args:
        indice1 (_type_): Indice de barco
        indice2 (_type_): Indice de barco
        indice3 (_type_): Indice de barco`
    """
    global tipo_barco, imagenes_config, direccion_barco
    tipo_barco=indice1
    imagenes_config=[]
    if indice1 == 1:
            imagenes_config.append(imagenes[indice1][direccion_barco])
    elif indice1 == 2:
            imagenes_config.append(imagenes[indice1][direccion_barco])
            imagenes_config.append(imagenes[indice2][direccion_barco])
    elif indice1 == 4:
            imagenes_config.append(imagenes[indice1][direccion_barco])
            imagenes_config.append(imagenes[indice2][direccion_barco])
            imagenes_config.append(imagenes[indice3][direccion_barco])
     
def colocar_barcos(i,j, matriz):
    """Coloca las imágenes de los barcos en los botones.

    Args:
        i (_type_): Posición en la fila de la matriz
        j (_type_): Posición en las columnas de la matriz.
        matriz (_type_): Matriz del jugador.
    """
    global tipo_barco, direccion_barco, imagenes_config, contador_destructor, contador_acorazado, contador_crucero
    if matriz[i][j]==0:
        if tipo_barco==1:
            if contador_destructor <= 5:
                matriz[i][j]=(tipo_barco*10)+direccion_barco
                botones[i][j].configure(image=imagenes_config[0])
                contador_destructor+=1
            else:
                messagebox.showerror(message="Limite de destructores alcanzado.", title="Mensaje")
        elif tipo_barco==2:
            if contador_crucero <= 3:
                if direccion_barco==1: 
                    if matriz[i][j-1]==0 and j != 0:
                        matriz[i][j]=(tipo_barco*10)+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i][j-1]=tipo_barco*10+direccion_barco
                        botones[i][j-1].configure(image=imagenes_config[0])
                        contador_crucero+=1
                    else:
                        messagebox.showerror(message="Coloca el crucero en otro sitio.", title="Mensaje")
                if direccion_barco==2: 
                    if matriz[i-1][j]==0 and i != 0:
                        matriz[i][j]=(tipo_barco*10)+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i-1][j]=tipo_barco*10+direccion_barco
                        botones[i-1][j].configure(image=imagenes_config[0])
                        contador_crucero+=1
                    else:
                        messagebox.showerror(message="Coloca el crucero en otro sitio.", title="Mensaje")
                if direccion_barco==3:
                    if matriz[i+1][j]==0 and i != len(matriz) -1:
                        matriz[i][j]=(tipo_barco*10)+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i+1][j]=tipo_barco*10+direccion_barco
                        botones[i+1][j].configure(image=imagenes_config[0])
                        contador_crucero+=1
                    else:
                        messagebox.showerror(message="Coloca el crucero en otro sitio.", title="Mensaje")
                if direccion_barco==0:
                    if matriz[i][j+1]==0 and j != len(matriz[0]) -1:
                        matriz[i][j]=(tipo_barco*10)+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i][j+1]=tipo_barco*10+direccion_barco
                        botones[i][j+1].configure(image=imagenes_config[0])

                        contador_crucero+=1
                    else:
                        messagebox.showerror(message="Coloca el crucero en otro sitio.", title="Mensaje")
            else:
                messagebox.showerror(message="Limite de cruceros alcanzado.", title="Mensaje")            
        elif tipo_barco == 4:
            if contador_acorazado <= 1:
                if direccion_barco==1:
                    if (matriz[i][j-1]==0 and matriz[i][j+1]==0) and (j != 0 and j != len(matriz[0])-1):
                        matriz[i][j]=tipo_barco*10+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i][j-1]=tipo_barco*10+direccion_barco
                        botones[i][j-1].configure(image=imagenes_config[0])
                        matriz[i][j+1]=tipo_barco*10+20+direccion_barco
                        botones[i][j+1].configure(image=imagenes_config[2])
                        contador_acorazado+=1
                    else:
                         messagebox.showerror(message="Coloca el acorazado en otro sitio.", title="Mensaje")
                if direccion_barco==2:
                    if (matriz[i-1][j]==0 and matriz[i+1][j]==0) and (i != 0 and i != len(matriz)-1):
                        matriz[i][j]=tipo_barco*10+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i-1][j]=tipo_barco*10+direccion_barco
                        botones[i-1][j].configure(image=imagenes_config[0])
                        matriz[i+1][j]=tipo_barco*10+20+direccion_barco
                        botones[i+1][j].configure(image=imagenes_config[2])
                        contador_acorazado+=1
                    else:
                        messagebox.showerror(message="Coloca el acorazado en otro sitio.", title="Mensaje")
                if direccion_barco ==3:
                    if (matriz[i-1][j]==0 and matriz[i+1][j]==0) and (i != 0 and i != len(matriz)-1):
                        matriz[i][j]=tipo_barco*10+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i+1][j]=tipo_barco*10+direccion_barco
                        botones[i+1][j].configure(image=imagenes_config[0])
                        matriz[i-1][j]=tipo_barco*10+20+direccion_barco
                        botones[i-1][j].configure(image=imagenes_config[2])
                        contador_acorazado+=1
                    else:
                        messagebox.showerror(message="Coloca el acorazado en otro sitio.", title="Mensaje")
                if direccion_barco ==0:
                    if (matriz[i][j-1]==0 and matriz[i][j+1]==0) and (j != 0 and j != len(matriz[0])-1):
                        matriz[i][j]=tipo_barco*10+10+direccion_barco
                        botones[i][j].configure(image=imagenes_config[1])
                        matriz[i][j+1]=tipo_barco*10+direccion_barco
                        botones[i][j+1].configure(image=imagenes_config[0])
                        matriz[i][j-1]=tipo_barco*10+20+direccion_barco
                        botones[i][j-1].configure(image=imagenes_config[2])
                        contador_acorazado+=1
                    else:
                        messagebox.showerror(message="Coloca el acorazado en otro sitio.", title="Mensaje")
            else:           
                messagebox.showerror(message="Limite de acorazados alcanzado.", title="Mensaje")            
    else:
        messagebox.showerror(message="Ya hay un barco en este posición.", title="Mensaje")
    
#Agua(0)
agua=Image.open("imagenes/más/agua_2.jpg")
agua=agua.resize((60, 60))
agua_tk=ImageTk.PhotoImage(agua)
#Destructor
destructor=Image.open("imagenes/barcos/destructor_agua.png")
destructor=destructor.resize((60, 60))
destructor_tk_derecha=ImageTk.PhotoImage(destructor)
destructor_tk_izquierda=ImageTk.PhotoImage(destructor.rotate(180))
destructor_tk_arriba=ImageTk.PhotoImage(destructor.rotate(90))
destructor_tk_abajo=ImageTk.PhotoImage(destructor.rotate(270))
#Crucero(Proa)
crucero_proa=Image.open("imagenes/barcos/crucero_proa_agua.png")
crucero_proa=crucero_proa.resize((60, 60))
crucero_proa_tk_derecha=ImageTk.PhotoImage(crucero_proa)
crucero_proa_tk_izquierda=ImageTk.PhotoImage(crucero_proa.rotate(180))
crucero_proa_tk_arriba=ImageTk.PhotoImage(crucero_proa.rotate(90))
crucero_proa_tk_abajo=ImageTk.PhotoImage(crucero_proa.rotate(270))
#Crucero(Popa)
crucero_popa=Image.open("imagenes/barcos/crucero_popa_agua.png")
crucero_popa=crucero_popa.resize((60, 60))
crucero_popa_tk_derecha=ImageTk.PhotoImage(crucero_popa)
crucero_popa_tk_izquierda=ImageTk.PhotoImage(crucero_popa.rotate(180))
crucero_popa_tk_arriba=ImageTk.PhotoImage(crucero_popa.rotate(90))
crucero_popa_tk_abajo=ImageTk.PhotoImage(crucero_popa.rotate(270))
#Acorazado(Proa)
acorazado_proa=Image.open("imagenes/barcos/Acorazado_proa_agua.png")
acorazado_proa=acorazado_proa.resize((60, 60))
acorazado_proa_tk_derecha=ImageTk.PhotoImage(acorazado_proa)
acorazado_proa_tk_izquierda=ImageTk.PhotoImage(acorazado_proa.rotate(180))
acorazado_proa_tk_arriba=ImageTk.PhotoImage(acorazado_proa.rotate(90))
acorazado_proa_tk_abajo=ImageTk.PhotoImage(acorazado_proa.rotate(270))
#Acorazado(Centro)
acorazado_centro=Image.open("imagenes/barcos/Acorazado_centro_agua.png")
acorazado_centro=acorazado_centro.resize((60, 60))
acorazado_centro_tk_derecha=ImageTk.PhotoImage(acorazado_centro)
acorazado_centro_tk_izquierda=ImageTk.PhotoImage(acorazado_centro.rotate(180))
acorazado_centro_tk_arriba=ImageTk.PhotoImage(acorazado_centro.rotate(90))
acorazado_centro_tk_abajo=ImageTk.PhotoImage(acorazado_centro.rotate(270))
#Acorazado(Proa)
acorazado_popa=Image.open("imagenes/barcos/Acorazado_popa_agua.png")
acorazado_popa=acorazado_popa.resize((60, 60))
acorazado_popa_tk_derecha=ImageTk.PhotoImage(acorazado_popa)
acorazado_popa_tk_izquierda=ImageTk.PhotoImage(acorazado_popa.rotate(180))
acorazado_popa_tk_arriba=ImageTk.PhotoImage(acorazado_popa.rotate(90))
acorazado_popa_tk_abajo=ImageTk.PhotoImage(acorazado_popa.rotate(270))

imagenes=[agua_tk,
    [destructor_tk_derecha,destructor_tk_izquierda,destructor_tk_arriba,destructor_tk_abajo],
    [crucero_proa_tk_derecha,crucero_proa_tk_izquierda,crucero_proa_tk_arriba,crucero_proa_tk_abajo],
    [crucero_popa_tk_derecha,crucero_popa_tk_izquierda,crucero_popa_tk_arriba,crucero_popa_tk_abajo],
    [acorazado_proa_tk_derecha,acorazado_proa_tk_izquierda,acorazado_proa_tk_arriba,acorazado_proa_tk_abajo],
    [acorazado_centro_tk_derecha,acorazado_centro_tk_izquierda,acorazado_centro_tk_arriba,acorazado_centro_tk_abajo],
    [acorazado_popa_tk_derecha,acorazado_popa_tk_izquierda,acorazado_popa_tk_arriba,acorazado_popa_tk_abajo]]