import tkinter as tk
from PIL import ImageTk, Image
from juego import *


def interfaz_juego(ventana:tk,matriz_jugador_1:list,matriz_jugador_2:list,jugador_1:list,jugador_2:list,turnos=0,area_cada_boton=0):
    """Función principal en el apartado de la interfaz de juego, desde aqui se crea todo los referente a la ventana donde se desarrollara el juego.

    Args:
        matriz_jugador_1 (list): La matriz de juego del primer jugador
        matriz_jugador_2 (list): La matriz de juego del segundo jugador
        jugador_1 (list): Jugador 1
        jugador_2 (list): Jugador 2
        turnos (int): En caso se inicie una partida guardada, para mantener el turno en el que se estaba
        area_cada_boton (int): En caso se inicie una partida guardada, se recibira el area que tenian el juego original
    """
    ventana.geometry("1000x700+200+200")
    jugador_1.append(True)
    jugador_1.append(1)
    jugador_1.append([6,4,2])
    jugador_2.append(False)
    jugador_2.append(2)
    jugador_2.append([6,4,2])
    #Frame juego
    frame_juego=tk.Frame(ventana)
    frame_juego.pack(fill="both",expand="TRUE")
    
    #Todo lo relacionado al menu_bar
    menu_bar=tk.Menu(ventana)
    opciones=tk.Menu(menu_bar)
    opciones=tk.Menu(menu_bar,tearoff=0)
    #Establecer las imagenes
    if(area_cada_boton<=0):
        divisor=25*len(matriz_jugador_1)*len(matriz_jugador_1[0])
        area_cada_boton=divisor//(len(matriz_jugador_1)*len(matriz_jugador_1[0]))
    else:
        pass
    images=prueba(area_cada_boton=area_cada_boton)
    interfaz_images=establecer_interfaz_images()
    #Opciones del menu_bar
    opciones.add_command(label="Guardar",command=lambda: guardar_archivo())
    opciones.add_command(label="Cargar",command=lambda: cargar())
    opciones.add_command(label="Tablas",command=lambda a=interfaz_images: tablas(interfaz_images=a))
    opciones.add_separator()
    opciones.add_command(label="Salir",command=lambda: salir())
    menu_bar.add_cascade(label="Opciones",menu=opciones)
    ventana.config(menu=menu_bar)
    #Fondo
    fondo=tk.Canvas(frame_juego,background="cyan",highlightthickness=0)
    fondo.pack(fill="both",expand="TRUE")
    #Frames
    #Frame 1
    frame_1=tk.Frame(frame_juego)
    canvas_1=tk.Canvas(frame_1,highlightthickness=0)
    canvas_1.pack()
    frame_1.place(x=20,y=70)
    mostrar_jugador_1=tk.Label(canvas_1,text=f"JUGADOR #1: {jugador_1[0]}",height=1,width=17,font=("Agency FB",16),bg="red")
    mostrar_jugador_1.pack(side="left",padx=10)
    destructor_1=tk.Label(canvas_1,image=interfaz_images[3])
    destructor_1.pack(side="left",padx=10)
    destructor_1_cantidad=tk.Label(canvas_1,text=f":{jugador_1[3][0]}",font=("Agency FB",12))
    destructor_1_cantidad.pack(side="left")
    crucero_1=tk.Label(canvas_1,image=interfaz_images[4])
    crucero_1.pack(side="left",padx=10)
    crucero_1_cantidad=tk.Label(canvas_1,text=f":{jugador_1[3][1]}",font=("Agency FB",12))
    crucero_1_cantidad.pack(side="left")
    acorazado_1=tk.Label(canvas_1,image=interfaz_images[5])
    acorazado_1.pack(side="left",padx=10)
    acorazado_1_cantidad=tk.Label(canvas_1,text=f":{jugador_1[3][2]}",font=("Agency FB",12))
    acorazado_1_cantidad.pack(side="left")
    acorazado_1_cantidad
    frame_list_1=[frame_1,canvas_1,mostrar_jugador_1,destructor_1,destructor_1_cantidad,crucero_1,crucero_1_cantidad,acorazado_1,acorazado_1_cantidad]
    
    #Frame 2
    frame_2=tk.Frame(frame_juego)
    frame_2.place(x=550,y=70)
    canvas_2=tk.Canvas(frame_2,background="white",highlightthickness=0)
    canvas_2.pack()
    mostrar_jugador_2=tk.Label(canvas_2,text=f"JUGADOR #2: {jugador_2[0]}",height=1,width=17,font=("Agency FB",16),bg="red")
    mostrar_jugador_2.pack(side="left",padx=10)
    destructor_2=tk.Label(canvas_2,image=interfaz_images[3])
    destructor_2.pack(side="left",padx=10)
    destructor_2_cantidad=tk.Label(canvas_2,text=f":{jugador_2[3][0]}",font=("Agency FB",12))
    destructor_2_cantidad.pack(side="left")
    crucero_2=tk.Label(canvas_2,image=interfaz_images[4])
    crucero_2.pack(side="left",padx=10)
    crucero_2_cantidad=tk.Label(canvas_2,text=f":{jugador_2[3][1]}",font=("Agency FB",12))
    crucero_2_cantidad.pack(side="left")
    acorazado_2=tk.Label(canvas_2,image=interfaz_images[5])
    acorazado_2.pack(side="left",padx=10)
    acorazado_2_cantidad=tk.Label(canvas_2,text=f":{jugador_2[3][2]}",font=("Agency FB",12))
    acorazado_2_cantidad.pack(side="left")
    frame_list_2=[frame_2,canvas_2,mostrar_jugador_2,destructor_2,destructor_2_cantidad,crucero_2,crucero_2_cantidad,acorazado_2,acorazado_2_cantidad]
    #Button messages
    a=Image.open("Imagenes/más/icon_messages.png")
    a=a.resize((50,50))
    a_tk=ImageTk.PhotoImage(a)
    messages=tk.Button(ventana,image=a_tk,command=lambda: messages_comand())
    messages.place(x=950,y=60)

    #Juego
    if(turnos>0):
        guardar_aqui(ma_1=matriz_jugador_1,ma_2=matriz_jugador_2,ju_1=jugador_1,ju_2=jugador_2,ven=ventana,imag=images,area=area_cada_boton,int_images=interfaz_images,tu=turnos,fr_1=frame_list_1,fr_2=frame_list_2)
    else:  
        guardar_aqui(ma_1=matriz_jugador_1,ma_2=matriz_jugador_2,ju_1=jugador_1,ju_2=jugador_2,ven=ventana,imag=images,area=area_cada_boton,int_images=interfaz_images,fr_1=frame_list_1,fr_2=frame_list_2)
        juego()

  
def prueba(area_cada_boton:int):
    """Función encargada de establecer las imagenes de los barcos.

    Args:
        area_cada_boton (int): El área que tendra cada botón 
    """
    barcos=["Imagenes/más/agua.jpg", #Agua(0)
            "Imagenes/barcos/destructor_agua.png", #Destructor(10,11,12,13)
            "Imagenes/barcos/destructor_agua_eliminado.png", #Destructor eliminado(14,15,16,17)
            "Imagenes/barcos/crucero_proa_agua.png", #Crucero proa(20,21,22,23)
            "Imagenes/barcos/crucero_proa_agua_eliminado.png", #Crucero proa eliminado(24,25,26,27)
            "Imagenes/barcos/crucero_popa_agua.png",  #Crucero popa (30,31,32,33)
            "Imagenes/barcos/crucero_popa_agua_eliminado.png",  #Crucero popa eliminado (34,35,36,37)
            "Imagenes/barcos/Acorazado_proa_agua.png", #Acorazado proa (40,41,42,43)
            "Imagenes/barcos/Acorazado_proa_agua_eliminado.png", #Acorazado proa eliminado (44,45,46,47)
            "Imagenes/barcos/Acorazado_centro_agua.png", #Acorazado centro (50,51,52,53)
            "Imagenes/barcos/Acorazado_centro_agua_eliminado.png", #Acorazado centro eliminado (54,55,56,57)
            "Imagenes/barcos/Acorazado_popa_agua.png", #Acorazado popa (60,61,62,63)
            "Imagenes/barcos/Acorazado_popa_agua_eliminado.png"] #Acorazado popa eliminado (64,65,66,67)
    imagenes=[]
    first_time=0
    p=True
    for a in barcos:
        image_A=Image.open(a)
        image_A=image_A.resize((area_cada_boton,area_cada_boton))
        image_tk_0=ImageTk.PhotoImage(image_A)
        if(first_time==0):
            imagenes.append(image_tk_0)
            first_time+=1
        else:
            image_tk_1=ImageTk.PhotoImage(image_A.rotate(180))
            image_tk_2=ImageTk.PhotoImage(image_A.rotate(90))
            image_tk_3=ImageTk.PhotoImage(image_A.rotate(270))
            if(p==True):
                imagenes.append([])
                imagenes[first_time].append(image_tk_0)
                imagenes[first_time].append(image_tk_1)
                imagenes[first_time].append(image_tk_2)
                imagenes[first_time].append(image_tk_3)
                p=False
            elif(p==False):
                imagenes[first_time].append(image_tk_0)
                imagenes[first_time].append(image_tk_1)
                imagenes[first_time].append(image_tk_2)
                imagenes[first_time].append(image_tk_3)
                first_time+=1
                p=True
    return(imagenes)

def establecer_interfaz_images():
    """Función encargada de establecer las imagenes principales de la interfaz base.
    """
    tal=["Imagenes/más/medalla_plata.png", 
         "Imagenes/más/medalla_oro.png",
         "Imagenes/fondo/tesoro-pirata.jpg",
         "Imagenes/más/Destructor.png",
         "Imagenes/más/Crucero.png",
         "Imagenes/más/Acorazado.png",
         "Imagenes/fondo/fondo_juego.jpg"]
    guardar=[]
    for e in tal:
        if(e==tal[2]):
            image_b=Image.open(e)
            image_b=image_b.resize((450,450))
            image_b_tk=ImageTk.PhotoImage(image_b)
            guardar.append(image_b_tk)  
        elif(e in (tal[3],tal[4],tal[5])):
            image_b=Image.open(e)
            image_b=image_b.resize((35,45))
            image_b_tk=ImageTk.PhotoImage(image_b)
            guardar.append(image_b_tk)
        else:
            image_b=Image.open(e)
            image_b=image_b.resize((1200,1200))
            image_b_tk=ImageTk.PhotoImage(image_b)
            guardar.append(image_b_tk)
    return(guardar)


