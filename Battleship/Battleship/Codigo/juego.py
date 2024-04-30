import tkinter as tk
import time
from PIL import ImageTk, Image

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"


#Guardar todo
matriz_jugador_1=[]
matriz_jugador_2=[]
jugador_1=[]
jugador_2=[]
ventana=None
imagenes=[]
area_cada_boton=0
mostrar_matriz_1=None
mostrar_matriz_2=None
turn_player_1=None
turn_player_2=None
turnos=0
interfaz_images=None
Frame_list_1=None
Frame_list_2=None

#Messages window
messages_matriz=[]




def guardar_aqui(ma_1=None,ma_2=None,ju_1=None,ju_2=None,ven=None,imag=None,area=0,int_images=None,tu=0,ms_matriz=None,new_game=True,fr_1=None,fr_2=None):
    """Esta función se encarga de establecer todas las variables en este archivo para evitar los problemas de estar pidiendo las variables a cada rato. En caso se intente cargar una partida guardada, se llamará a esta función.

    Args:
        ma_1 (_type_, optional): La matriz del jugador 1.
        ma_2 (_type_, optional): La matriz del jugador 2.
        ju_1 (_type_, optional): Lista del primer jugador.
        ju_2 (_type_, optional): Lista del segundo jugador.
        ven (_type_, optional): La ventana del juego.
        imag (_type_, optional): Imagenes de la lista de barcos.
        area (int, optional): Área necesaria para establecer los botones.
        int_images (_type_, optional): Imagenes de la interfaz.
        tu (int, optional): Turno actual de la partida, se recibira solo si se está intentando cargar una partida.
        ms_matriz (_type_, optional): matriz de los mensajes, se recibira solo si se está intentando cargar una partida.
        new_game (bool, optional): Variable que indica si se esta empezando nueva partida o se esta cargando una.
        fr_1 (_type_, optional): Frame número uno.
        fr_2 (_type_, optional): Frame número dos.
    """
    global matriz_jugador_1,matriz_jugador_2,jugador_1,jugador_2,ventana,imagenes,area_cada_boton,interfaz_images,turnos,messages_matriz,Frame_list_1,Frame_list_2
    if(tu>0):
        turnos=tu
    else:
        pass
    if(new_game==True):
        imagenes=imag
        ventana=ven
        area_cada_boton=area
        jugador_1=ju_1
        jugador_2=ju_2
        matriz_jugador_1=ma_1
        matriz_jugador_2=ma_2
        interfaz_images=int_images
        Frame_list_1=fr_1
        Frame_list_2=fr_2

    else:
        matriz_jugador_1=ma_1
        matriz_jugador_2=ma_2
        jugador_1=ju_1
        jugador_2=ju_2
        turnos=tu
        messages_matriz=ms_matriz
        area_cada_boton=area
        juego()
    

def juego(delete_button=tk,delete_label=tk):
    global matriz_jugador_1,matriz_jugador_2,jugador_1,jugador_2,ventana,imagenes,area_cada_boton,mostrar_matriz_1,mostrar_matriz_2,turn_player_1,turn_player_2,interfaz_images,Frame_list_1,Frame_list_2
    """Desde aqui se llamara a otras funciones para el funcionamiento del juego, además se encarga de determinar constantemente si la condición de victoria se cumplió.

    Args:
        matriz_jugador_1 (list): Matriz del jugador 1.
        matriz_jugador_2 (list): Matriz del jugador 2.
        jugador_1 (list): Lista del jugador 1.
        jugador_2 (list): Lista del jugador 2.
    """
    #Prueba
    
    try:
        delete_button.destroy()
        delete_label.destroy()
    except:
        pass
    victory=True
    for v in matriz_jugador_1:
        for e in v:
            if(e in (10,11,12,13,20,21,22,23,30,31,32,33,40,41,42,43,50,51,52,53,60,61,62,63)):
                victory=False
            else:
                pass
    if(victory==True):
        victoria(winner=jugador_2,losser=jugador_1,interfaz_images=interfaz_images)
    else:
        for v in matriz_jugador_2:
            for e in v:
                if(e in (10,11,12,13,20,21,22,23,30,31,32,33,40,41,42,43,50,51,52,53,60,61,62,63)):
                    victory=False
                else:
                    pass
        if(victory==True):
            victoria(winner=jugador_2,losser=jugador_1,interfaz_images=interfaz_images)
        else:
            pass
    #Naves restantes
    Frame_list_1[4].config(text=f":{jugador_1[3][0]}")
    Frame_list_1[6].config(text=f":{jugador_1[3][1]}")
    Frame_list_1[8].config(text=f":{jugador_1[3][2]}")
    Frame_list_2[4].config(text=f":{jugador_2[3][0]}")
    Frame_list_2[6].config(text=f":{jugador_2[3][1]}")
    Frame_list_2[8].config(text=f":{jugador_2[3][2]}")

    if(jugador_1[1]==True and jugador_2[1]==False):
        turn_player_1=tk.Label(ventana,text=f"Es el turno de {jugador_1[0]}.",font=("Agency FB",20),height=1,width=20,fg="black",bg="yellow",state="disabled")
        turn_player_1.place(x=5,y=450)
    elif(jugador_2[1]==True and jugador_1[1]==False):
        turn_player_2=tk.Label(ventana,text=f"Es el turno de {jugador_2[0]}.",font=("Agency FB",20),height=1,width=20,fg="black",bg="yellow",state="disabled")
        turn_player_2.place(x=5,y=450) 
    mostrar_matriz_1=None
    mostrar_matriz_2=None
    matriz_jugador_1=mover_barcos(matriz_jugador=matriz_jugador_1)
    matriz_jugador_2=mover_barcos(matriz_jugador=matriz_jugador_2)
    mostrar_matriz_1=actualizar(matriz_jugador_1=matriz_jugador_1,ventana=ventana,en_x=20,en_y=70,area_cada_boton=area_cada_boton,imagenes=imagenes,jugador=jugador_1)
    mostrar_matriz_2=actualizar(matriz_jugador_1=matriz_jugador_2,ventana=ventana,en_x=550,en_y=70,area_cada_boton=area_cada_boton,imagenes=imagenes,jugador=jugador_2)

    ventana.mainloop()

def mover_barcos(matriz_jugador:list):
    """Función encargada del movimiento de los barcos, aparte de la matriz recibida, importa globalmente los turnos.

    Args:
        matriz_jugador (list): Matriz del jugador al que se le van a mover los barcos.
    """
    global turnos
    if(turnos%2==0 and not turnos==0):
        vertical_contador=0
        horizontal_contador=0
        for v in matriz_jugador:
            for h in v:
                match h:
                    case 10|11|12|13:
                        borde=False
                        x=0
                        y=0
                        y_2=0
                        
                        escape=0
                        original_h=horizontal_contador
                        original_v=vertical_contador
                        while(not escape==2):
                            if(h==10):
                                if(horizontal_contador==len(matriz_jugador[vertical_contador])-1):
                                    borde=True
                                    x=1
                                else:
                                    x=1
                            elif(h==11):
                                if(horizontal_contador==0):
                                    borde=True
                                    x=-1
                                else:
                                    x=-1
                            elif(h==12):
                                if(vertical_contador==0):
                                    borde=True
                                    y=-1
                                    y_2=1
                                else:
                                    y=-1
                                    y_2=1
                            elif(h==13):
                                if(vertical_contador==len(matriz_jugador_1)-1):
                                    borde=True
                                    y=1
                                    y_2=-1
                                else:
                                    y=1
                                    y_2=-1
                            if(borde==True):
                                matriz_jugador[vertical_contador][horizontal_contador]=(h+x+y_2)*10
                                break
                            try:
                                if(matriz_jugador[vertical_contador+y][horizontal_contador+x]==0):
                                    matriz_jugador[vertical_contador+y][horizontal_contador+x]=h
                                    matriz_jugador[vertical_contador][horizontal_contador]=0
                                    horizontal_contador+=x
                                    vertical_contador+=y
                                    escape+=1
                                    if(escape==2):
                                        matriz_jugador[vertical_contador][horizontal_contador]=h*10
                                    else:
                                        pass
                                else:
                                    matriz_jugador[vertical_contador][horizontal_contador]=(h+x+y_2)*10
                                    break
                            except:
                                matriz_jugador[vertical_contador][horizontal_contador]=(h+x+y_2)*10
                                break
                        horizontal_contador=original_h
                        vertical_contador=original_v
                        horizontal_contador+=1
                    case 20|21|22|23|24|25|26|27:
                        borde=False
                        x=0
                        y=0
                        y_2=0
                        if(h in (20,24)):
                            if(horizontal_contador==len(matriz_jugador[vertical_contador])-1):
                                borde=True
                                x=1
                            else:
                                x=1
                        elif(h in (21,25)):
                            if(horizontal_contador==0):
                                borde=True
                                x=-1
                            else:
                                x=-1
                        elif(h in (22,26)):
                            if(vertical_contador==0):
                                borde=True
                                y=-1
                                y_2=1
                            else:
                                y=-1
                                y_2=1
                        elif(h in (23,27)):
                            if(vertical_contador==len(matriz_jugador_1)-1):
                                borde=True
                                y=1
                                y_2=-1
                            else:
                                y=1
                                y_2=-1
                        if(matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1] in (34,35,36,37) or h in(24,25,26,27)):
                            matriz_jugador[vertical_contador][horizontal_contador]=h*10
                            save=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                            matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=save*10
                        else:
                            if(borde==True):
                                save=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=(h+x+y_2)*10
                                matriz_jugador[vertical_contador][horizontal_contador]=(save+x+y_2)*10
                            else:
                                try:
                                    if(matriz_jugador[vertical_contador+y][horizontal_contador+x]==0):
                                        save=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                        matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=0
                                        matriz_jugador[vertical_contador+y][horizontal_contador+x]=h*10
                                        matriz_jugador[vertical_contador][horizontal_contador]=save*10
                                    else:
                                        save=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                        matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=(h+x+y_2)*10
                                        matriz_jugador[vertical_contador][horizontal_contador]=(save+x+y_2)*10
                                        
                                except:
                                    save=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                    matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=(h+x+y_2)*10
                                    matriz_jugador[vertical_contador][horizontal_contador]=(save+x+y_2)*10
                        horizontal_contador+=1
                    case 40|41|42|43|44|45|46|47:
                        borde=False
                        x=0
                        y=0
                        y_2=0
                        if(h in (40,44)):
                            if(horizontal_contador==len(matriz_jugador[vertical_contador])-1):
                                borde=True
                                x=1
                            else:
                                x=1
                        elif(h in (41,45)):
                            if(horizontal_contador==0):
                                borde=True
                                x=-1
                            else:
                                x=-1
                        elif(h in (42,46)):
                            if(vertical_contador==0):
                                borde=True
                                y=-1
                                y_2=1
                            else:
                                y=-1
                                y_2=1
                        elif(h in (43,47)):
                            if(vertical_contador==len(matriz_jugador_1)-1):
                                borde=True
                                y=1
                                y_2=-1
                            else:
                                y=1
                                y_2=-1
                        if(matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1] in (54,55,56,57) or matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2] in (64,65,66,67) or h in (44,45,46,47)):
                            matriz_jugador[vertical_contador][horizontal_contador]=h*10
                            save_1=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                            save_2=matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]
                            matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=save_1*10
                            matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]=save_2*10
                        else:
                            if(borde==True):
                                save_1=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                save_2=matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]
                                matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]=(h+x+y_2)*10
                                matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=(save_1+x+y_2)*10
                                matriz_jugador[vertical_contador][horizontal_contador]=(save_2+x+y_2)*10
                            else:
                                try:
                                    if(matriz_jugador[vertical_contador+y][horizontal_contador+x]==0):
                                        save_1=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                        save_2=matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]
                                        matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]=0
                                        matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=save_2*10
                                        matriz_jugador[vertical_contador+y][horizontal_contador+x]=h*10
                                        matriz_jugador[vertical_contador][horizontal_contador]=save_1*10
                                    else:
                                        save_1=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                        save_2=matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]
                                        matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]=(h+x+y_2)*10
                                        matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=(save_1+x+y_2)*10
                                        matriz_jugador[vertical_contador][horizontal_contador]=(save_2+x+y_2)*10
                                except:
                                    save_1=matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]
                                    save_2=matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]
                                    matriz_jugador[vertical_contador+y*-2][horizontal_contador+x*-2]=(h+x+y_2)*10
                                    matriz_jugador[vertical_contador+y*-1][horizontal_contador+x*-1]=(save_1+x+y_2)*10
                                    matriz_jugador[vertical_contador][horizontal_contador]=(save_2+x+y_2)*10
                        horizontal_contador+=1
                    case 14|15|16|17:
                        matriz_jugador[vertical_contador][horizontal_contador]=h*10
                        horizontal_contador+=1
                    case _:
                        horizontal_contador+=1
            vertical_contador+=1
            horizontal_contador=0
        vertical_contador=0
        horizontal_contador=0
        while(not vertical_contador==len(matriz_jugador)):
            while(not horizontal_contador==len(matriz_jugador[0])):
                matriz_jugador[vertical_contador][horizontal_contador]//=10
                horizontal_contador+=1
            vertical_contador+=1
            horizontal_contador=0
    else:
        pass
    return(matriz_jugador)

def victoria(winner:list,losser:list,interfaz_images:list,tablas=False):
    """Cuando la condición de victoria se cumplió, se llama a esta funcion para abrir la pantalla de victoria. Además se otorga la posibilidad de volver al menú o salir del juego.

    Args:
        winner (list): Jugador que ganó la partida, en caso de empate aparecen igual.
        losser (list): Jugador que perdió la partida, en caso de empate aparecen igual.
        interfaz_images (list): Recibe la lista de imagenes para colocarlas en la ventana de victoria.
        tablas (bool, optional): En caso de establecerce tablas, la función se encarga de evaluar la puntuación de ambos, y si hubo empate ambos jugadores salen igual.
    """
    victory_window=tk.Toplevel()
    victory_window.geometry("400x400+700+200")
    if(tablas==False):
        victory_window.title("Winner, winner, chicken dinner")
        #FONDO
        fondo = tk.Label(victory_window, image=interfaz_images[2])
        fondo.pack(fill=tk.BOTH, expand=tk.TRUE)
        #Primer lugar
        medalla_oro_label=tk.Label(victory_window,image=interfaz_images[1],width=80,height=80) 
        medalla_oro_label.place(x=10,y=80)
        ganador_label=tk.Label(victory_window,text=f"GANADOR: {winner[0]}. \n//Con una puntuación de {winner[4]}",font=("Times New Roman",12,"bold"),height=3,width=30,bg="blue",fg="gold2")
        ganador_label.place(x=80,y=80)
        #Segundo lugar
        medalla_plata_label=tk.Label(victory_window,image=interfaz_images[0],width=80,height=80) 
        medalla_plata_label.place(x=10,y=180)
        segundo_lugar_label=tk.Label(victory_window,text=f"SEGUNDO LUGAR: {losser[0]}. \n//Con una puntuación de {losser[4]}",font=("Times New Roman",12,"bold"),height=3,width=30,bg="red",fg="LightSteelBlue4")
        segundo_lugar_label.place(x=80,y=180)
        #Botones de salir del juego y volver al menú
        button_exit=tk.Button( victory_window,text="SALIR",width=12,height=4,command=lambda a=1: volver(opcion=a))
        button_exit.place(x=80,y=300)
        button_volver=tk.Button( victory_window,text="VOLVER AL MENÚ",width=15,height=4,command=lambda a=2: volver(opcion=a))
        button_volver.place(x=200,y=300)
        victory_window.mainloop()
    else:
        victory_window.title("Tablas, tablas, not chicken for dinner")
        #FONDO
        fondo = tk.Label(victory_window, image=interfaz_images[2])
        fondo.pack(fill=tk.BOTH, expand=tk.TRUE)
        #Primer lugar
        medalla_oro_label=tk.Label(victory_window,image=interfaz_images[1],width=80,height=80) 
        medalla_oro_label.place(x=10,y=80)
        ganador_label=tk.Label(victory_window,text=f"TABLAS: {winner[0]}. \n//Con una puntuación de {winner[4]}",font=("Times New Roman",12,"bold"),height=3,width=30,bg="blue",fg="gold2")
        ganador_label.place(x=80,y=80)
        #Segundo lugar
        medalla_plata_label=tk.Label(victory_window,image=interfaz_images[1],width=80,height=80) 
        medalla_plata_label.place(x=10,y=180)
        segundo_lugar_label=tk.Label(victory_window,text=f"TABLAS: {losser[0]}. \n//Con una puntuación de {losser[4]}",font=("Times New Roman",12,"bold"),height=3,width=30,bg="red",fg="LightSteelBlue4")
        segundo_lugar_label.place(x=80,y=180)
        #Botones de salir del juego y volver al menú
        button_exit=tk.Button( victory_window,text="SALIR",width=12,height=4,command=lambda a=1: volver(opcion=a))
        button_exit.place(x=80,y=300)
        button_volver=tk.Button( victory_window,text="VOLVER AL MENÚ",width=15,height=4,command=lambda a=2: volver(opcion=a))
        button_volver.place(x=200,y=300)
        victory_window.mainloop()


def volver(opcion=0):
    """Función pequeña que se encarga de salir o volver al menú principal.

    Args:
        opcion (int, optional): La opción uno se sale del juego, y la dos devuelve a los usuarios al menú
    """
    if(opcion==1):
        exit()
    elif(opcion==2):
        print("pendejo no hace nada *2")

def comando_botones(jugador:list,x:int,y:int):
    """La función más grande del juego, y la responsable de comprobar si a la hora de recibir un disparo, este dio en el blanco o no. Por supuesto tambien se encarga de desabilitar los botones del jugador que está jugando.

    Args:
        jugador (list): Lista del jugador dueño de los botones.
        x (int): Ubicación en x del botón.
        y (int): Ubicación en y del botón.
    """
    global matriz_jugador_1,matriz_jugador_2,messages_matriz,ventana,turn_player_1,turn_player_2,jugador_1,jugador_2,turnos
    if(jugador[1]==True):
        print("Pendejo no hace nada")
    else:
        if(jugador[2]==1):
            p=matriz_jugador_1[y][x]
            how=1
        else:
            p=matriz_jugador_2[y][x]
            how=2
        match p:
            case 0:  #Golpe directo al mar
                #Aqui iria el mensaje de fallo, se colocaria una x en el boton correspondiente indicando el ultimo lugar donde se disparó, y más mamadas que hay que poner aqui.
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(MISS) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) falló.\n")
                    miss_label=tk.Label(ventana,text=f"El disparo realizado por el jugador {jugador_2[0]} falló.",font=("Agency FB",20),height=1,width=40,fg="red",bg="cyan")
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(MISS) El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) falló.\n")
                    miss_label=tk.Label(ventana,text=f"El disparo realizado por el jugador {jugador_1[0]} falló.",font=("Agency FB",20),height=1,width=40,fg="red",bg="cyan")
                    jugador[1]=True
                    jugador_1[1]=False
                miss_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=miss_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 10|11|12|13:  #Golpe directo al destructor
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) logró alcanzar a un destructor (GOLPE DE GRACIA: +1 PUNTO).\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_2[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_1[y][x]+=4
                    jugador[1]=True
                    jugador_2[1]=False
                    try:
                        jugador_2[4]+=1
                        jugador_1[3][0]-=1
                    except:
                        jugador_2.append(1)
                        jugador_1[3][0]-=1
                else:
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) logró alcanzar a un destructor (GOLPE DE GRACIA: +1 PUNTO).\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_1[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_2[y][x]+=4
                    jugador[1]=True
                    jugador_1[1]=False
                    try:
                        jugador_1[4]+=1
                        jugador_2[3][0]-=1
                    except:
                        jugador_1.append(1)
                        jugador_2[3][0]-=1
                shot_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=shot_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 20|21|22|23:  #Golpe directo a la proa del crucero
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) logró alcanzar a una parte del crucero.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_2[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_1[y][x]+=4
                    if(matriz_jugador_1[y][x]%10==4):
                        if(matriz_jugador_1[y][x-1]==34):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==5):
                        if(matriz_jugador_1[y][x+1]==35):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==6):
                        if(matriz_jugador_1[y+1][x]==36):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==7):
                        if(matriz_jugador_1[y-1][x]==37):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos). \n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) logró alcanzar a un destructor.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_1[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_2[y][x]+=4
                    if(matriz_jugador_2[y][x]%10==4):
                        if(matriz_jugador_2[y][x-1]==34):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos). \n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==5):
                        if(matriz_jugador_2[y][x+1]==35):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==6):
                        if(matriz_jugador_2[y+1][x]==36):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==7):
                        if(matriz_jugador_2[y-1][x]==37):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_1[1]=False
                shot_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=shot_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 30|31|32|33:  #Golpe directo a la popa del crucero
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) logró alcanzar a una parte del crucero.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_2[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_1[y][x]+=4
                    if(matriz_jugador_1[y][x]%10==4):
                        if(matriz_jugador_1[y][x+1]==24):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1

                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==5):
                        if(matriz_jugador_1[y][x-1]==25):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==6):
                        if(matriz_jugador_1[y-1][x]==26):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==7):
                        if(matriz_jugador_1[y+1][x]==27):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_2[4]+=2
                                jugador_1[3][1]-=1
                            except:
                                jugador_2.append(2)
                                jugador_1[3][1]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(SHOT)El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) logró alcanzar a una parte del crucero.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_1[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_2[y][x]+=4
                    if(matriz_jugador_2[y][x]%10==4):
                        if(matriz_jugador_2[y][x+1]==24):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==5):
                        if(matriz_jugador_2[y][x-1]==25):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==6):
                        if(matriz_jugador_2[y-1][x]==26):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==7):
                        if(matriz_jugador_2[y+1][x]==27):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos). \n")
                            try:
                                jugador_1[4]+=2
                                jugador_2[3][1]-=1
                            except:
                                jugador_1.append(2)
                                jugador_2[3][1]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_1[1]=False
                shot_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=shot_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 40|41|42|43:  #Golpe directo a la proa del acorazado
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) logró alcanzar a una parte del acorazado. \n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_2[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_1[y][x]+=4
                    if(matriz_jugador_1[y][x]%10==4):
                        if(matriz_jugador_1[y][x-1]==54 and matriz_jugador_1[y][x-2]==64):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==5):
                        if(matriz_jugador_1[y][x+1]==55 and matriz_jugador_1[y][x+2]==65):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos). \n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==6):
                        if(matriz_jugador_1[y+1][x]==56 and matriz_jugador_1[y+2][x]==66):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==7):
                        if(matriz_jugador_1[y-1][x]==57 and matriz_jugador_1[y-2][x]==67):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos). \n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) logró alcanzar a un acorazado.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_1[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_2[y][x]+=4
                    if(matriz_jugador_2[y][x]%10==4):
                        if(matriz_jugador_2[y][x-1]==54 and matriz_jugador_2[y][x-2]==64):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos). \n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==5):
                        if(matriz_jugador_2[y][x+1]==55 and matriz_jugador_2[y][x+2]==65):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1

                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==6):
                        if(matriz_jugador_2[y+1][x]==56 and matriz_jugador_2[y+2][x]==66):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==7):
                        if(matriz_jugador_2[y-1][x]==57 and matriz_jugador_2[y-2][x]==67):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_1[1]=False
                shot_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=shot_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 50|51|52|53:  #Golpe directo al centro del acorazado
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) logró alcanzar a una parte del acorazado.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_2[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_1[y][x]+=4
                    if(matriz_jugador_1[y][x]%10==4):
                        if(matriz_jugador_1[y][x+1]==44 and matriz_jugador_1[y][x-1]==64):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==5):
                        if(matriz_jugador_1[y][x-1]==45 and matriz_jugador_1[y][x+1]==65):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==6):
                        if(matriz_jugador_1[y-1][x]==46 and matriz_jugador_1[y+1][x]==66):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==7):
                        if(matriz_jugador_1[y+1][x]==47 and matriz_jugador_1[y-1][x]==67):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(SHOT)El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) logró alcanzar a un acorazado.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_1[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_2[y][x]+=4
                    if(matriz_jugador_2[y][x]%10==4):
                        if(matriz_jugador_2[y][x+1]==44 and matriz_jugador_2[y][x-1]==64):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==5):
                        if(matriz_jugador_2[y][x-1]==45 and matriz_jugador_2[y][x+1]==65):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==6):
                        if(matriz_jugador_2[y-1][x]==46 and matriz_jugador_2[y+1][x]==66):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==7):
                        if(matriz_jugador_2[y+1][x]==47 and matriz_jugador_2[y-1][x]==67):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos). \n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_1[1]=False
                shot_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=shot_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 60|61|62|63:  #Golpe directo a la popa del acorazado
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) logró alcanzar a una parte del acorazado.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_2[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_1[y][x]+=4
                    if(matriz_jugador_1[y][x]%10==4):
                        if(matriz_jugador_1[y][x+1]==54 and matriz_jugador_1[y][x+2]==44):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos). \n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==5):
                        if(matriz_jugador_1[y][x-1]==55 and matriz_jugador_1[y][x-2]==45):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==6):
                        if(matriz_jugador_1[y-1][x]==56 and matriz_jugador_1[y-2][x]==46):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_1[y][x]%10==7):
                        if(matriz_jugador_1[y+1][x]==57 and matriz_jugador_1[y+2][x]==47):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_2[4]+=3
                                jugador_1[3][2]-=1
                            except:
                                jugador_2.append(3)
                                jugador_1[3][2]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(SHOT) El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) logró alcanzar a un acorazado.\n")
                    shot_label=tk.Label(ventana,text=f"El disparo del jugador {jugador_1[0]} dio en el blanco.",font=("Agency FB",20),height=1,width=40,fg="green",bg="cyan")
                    matriz_jugador_2[y][x]+=4
                    if(matriz_jugador_2[y][x]%10==4):
                        if(matriz_jugador_2[y][x+1]==54 and matriz_jugador_2[y][x+2]==44):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos). \n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==5):
                        if(matriz_jugador_2[y][x-1]==55 and matriz_jugador_2[y][x-2]==45):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==6):
                        if(matriz_jugador_2[y-1][x]==56 and matriz_jugador_2[y-2][x]==46):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+3 puntos).\n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    elif(matriz_jugador_2[y][x]%10==7):
                        if(matriz_jugador_2[y+1][x]==57 and matriz_jugador_2[y+2][x]==47):
                            messages_matriz.append(f"(SHOT) Golpe de gracia (+2 puntos). \n")
                            try:
                                jugador_1[4]+=3
                                jugador_2[3][2]-=1
                            except:
                                jugador_1.append(3)
                                jugador_2[3][2]-=1
                        else:
                            pass
                    jugador[1]=True
                    jugador_1[1]=False
                shot_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=shot_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
            case 14|15|16|17|24|25|26|27|34|35|36|37|44|45|46|47|54|55|56|57|64|65|66|67: #Golpe directo a una parte ya eliminada
                print(x,y)
                try:
                    turn_player_1.destroy()
                except:    
                    try:
                        turn_player_2.destroy()
                    except:
                        pass
                if(how==1):
                    messages_matriz.append(f"(MISS) El disparo del jugador {jugador_2[0]} realizado en las casillas ({x},{y}) falló. \n")
                    miss_label=tk.Label(ventana,text=f"El disparo realizado por el jugador {jugador_2[0]} falló.",font=("Agency FB",20),height=1,width=40,fg="red",bg="cyan")
                    jugador[1]=True
                    jugador_2[1]=False
                else:
                    messages_matriz.append(f"(MISS)El disparo del jugador {jugador_1[0]} realizado en las casillas ({x},{y}) falló. \n")
                    miss_label=tk.Label(ventana,text=f"El disparo realizado por el jugador {jugador_1[0]} falló.",font=("Agency FB",20),height=1,width=40,fg="red",bg="cyan")
                    jugador[1]=True
                    jugador_1[1]=False
                miss_label.place(x=5,y=450)
                next_turn=tk.Button(ventana,text="Siguiente turno",font=("Agency FB",20),height=1,width=15,bg="yellow",fg="green")
                next_turn.config(command=lambda button=next_turn,label=miss_label:juego(delete_button=button,delete_label=label))
                next_turn.place(x=5,y=490)
                turnos+=1
    
def messages_comand(verificador=0,ventan=tk):
    """Función que se encarga de crear la ventana donde se estaran colocando los mensajes de la partida.

    Args:
        verificador (int, optional): verficador para volver de forma recursiva en esta misma función.
        ventan (_type_, optional): La ventana que volvera de forma recursiva por si se selecciona la opción de eliminar la ventana.
    """
    global messages_matriz
    if(verificador==0):
        messages_window=tk.Toplevel()
        messages_window.title("Messages")
        messages_window.geometry("400x400")
        exit_messages=tk.Button(messages_window,text="Exit",command=lambda: messages_comand(verificador=1,ventan=messages_window),height=1,width=4)
        exit_messages.place(x=10,y=350)
        finally_messages=tk.Text(messages_window,font=('calibre',10,'normal'),relief="solid",width=50,height=20,padx=10,pady=10)
        finally_messages.place(x=15,y=0)
        sumador=0
        for e in messages_matriz:
            sumador+=1
            finally_messages.insert(tk.END,e)
        messages_window.mainloop()
    else:
        ventan.destroy()
    
def actualizar(matriz_jugador_1:list,jugador:list,ventana:tk,en_x:int,en_y:int,area_cada_boton:int,imagenes:list):
    """Segunda función importante encargado de establecer los botones junto a las imagenes en la ventana.

    Args:
        matriz_jugador_1 (list): Matriz del jugador a establecer.
        jugador (list): Lista del jugador.
        ventana (tk): La ventana donde se colocaran los botones.
        en_x (int): Ubicación en x del botón. 
        en_y (int): Ubicación en y del botón.
        area_cada_boton (int): El área que tendra cada botón.
        imagenes (list): Lista con las imagenes de los barcos.
    """
    #Añadir listas al mostrar matriz
    mostrar_matriz=[]
    añadir_contador=0
    while(not añadir_contador==len(matriz_jugador_1)):
        mostrar_matriz.append([])
        añadir_contador+=1
    #Todo el proceso de colocarle las imagenes a cada botón
    colocador_matriz_mostrar=0
    contador_horizontal=0
    for i in matriz_jugador_1:
        for p in i:
            colocar=p
            if(jugador[1]==True):
                pass
            else:
                colocar=0
            match colocar:
                case 0:
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[0],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y)))
                    contador_horizontal+=1
                case 10|11|12|13|14|15|16|17:
                    direccion=colocar%10
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[1][direccion],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y)))
                    contador_horizontal+=1
                case 20|21|22|23|24|25|26|27:
                    direccion=colocar%10
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[2][direccion],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y)))
                    contador_horizontal+=1
                case 30|31|32|33|34|35|36|37:
                    direccion=colocar%10
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[3][direccion],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y)))
                    contador_horizontal+=1
                case 40|41|42|43|44|45|46|47:
                    direccion=colocar%10
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[4][direccion],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y)))
                    contador_horizontal+=1
                case 50|51|52|53|54|55|56|57:
                    direccion=colocar%10
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[5][direccion],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y)))
                    contador_horizontal+=1
                case 60|61|62|63|64|65|66|67:
                    direccion=colocar%10
                    mostrar_matriz[colocador_matriz_mostrar].append(tk.Button(ventana,image=imagenes[6][direccion],command=lambda x=contador_horizontal,y=colocador_matriz_mostrar,juga=jugador:comando_botones(jugador=juga,x=x,y=y))) 
                    contador_horizontal+=1    
                #Recuerda que aqui siguen el resto de casos
        colocador_matriz_mostrar+=1
        contador_horizontal=0
        
    en_y+=50
    guardar_x=en_x
    for columna in mostrar_matriz:
        en_x=guardar_x
        for fila in columna:
            fila.place(x=en_x,y=en_y,height=area_cada_boton, width=area_cada_boton)
            en_x+=area_cada_boton
        en_y+=area_cada_boton
    return(mostrar_matriz)

def salir(verificador=0,ventan=tk):  
    """Función que crea una ventada y da la opción de volver al menú principal.

    Args:
        verificador (int, optional): Verficador para volver de forma recursiva en la misma función.
        ventan (_type_, optional): Ventana que volvera de forma recursiva para eliminarse asi misma.
    """
    if(verificador==0):
        ventana_salir=tk.Toplevel()
        ventana_salir.geometry("250x100+750+400")
        texto_salir=tk.Label(ventana_salir,text="¿Quieres salir al menú principal?",height=1,width=30)
        texto_salir.pack(side="top")
        boton_salir_si=tk.Button(ventana_salir,text="Si",command=lambda: salir(verificador=1,ventan=ventana_salir),height=1,width=4)
        boton_salir_si.pack(side="left",padx=10)
        boton_salir_no=tk.Button(ventana_salir,text="No",command=lambda: salir(verificador=2,ventan=ventana_salir),height=1,width=4)
        boton_salir_no.pack(side="right",padx=10)
        ventana_salir.mainloop()
    elif(verificador==1):
        exit()
    elif(verificador==2):
        ventan.destroy()



def cargar():
    """Función para la creación de una ventana que da la opción de cargar una partida, para cargar una partida se requiere recordar el nombre del archivo.
    """
    cargar_ventana=tk.Toplevel()
    cargar_ventana.geometry("300x150+750+400")
    cargar_ventana.title("Cargar partida")
    guardar=tk.StringVar()
    #Label
    nombre_archivo_label=tk.Label(cargar_ventana,text="Escriba el nombre del archivo a cargar: ",font=("Times New Roman",15))
    nombre_archivo_label.place(x=20,y=50)
    #Entry para recibir nombre de archivo
    nombre_archivo_entry=tk.Entry(cargar_ventana,textvariable=guardar)
    nombre_archivo_entry.place(x=20,y=80)
    #Botones
    boton_guardar=tk.Button(cargar_ventana,text="Cargar",width=10,height=3,command=lambda save_name=guardar, v=cargar_ventana, n=1: guardar_y_cargar_archivo_interno(save=save_name,ventana=v,opcion=n))
    boton_guardar.place(x=210,y=90)


def guardar_archivo():
    """Función encargada del guardardo de partidas.
    """
    guardar_ventana=tk.Toplevel()
    guardar_ventana.geometry("300x150+750+400")
    guardar_ventana.title("Guardar partida")
    guardar=tk.StringVar()
    #Label
    nombre_archivo_label=tk.Label(guardar_ventana,text="Escriba el nombre del archivo: ",font=("Times New Roman",15))
    nombre_archivo_label.place(x=20,y=50)
    #Entry para recibir nombre de archivo
    nombre_archivo_entry=tk.Entry(guardar_ventana,textvariable=guardar)
    nombre_archivo_entry.place(x=20,y=80)
    #Botones
    boton_guardar=tk.Button(guardar_ventana,text="Guardar",width=10,height=3,command=lambda save_name=guardar, v=guardar_ventana, n=2: guardar_y_cargar_archivo_interno(save=save_name,ventana=v,opcion=n))
    boton_guardar.place(x=210,y=90)

def guardar_y_cargar_archivo_interno(save,ventana:tk,opcion:int):
    """Las funciones que se encargan del guardado y la carga llamaran a esta función.

    Args:
        save (_type_): Nombre del archivo.
        ventana (tk): Ventana de guardado o de carga.
        opcion (int): Si se requiere guardar una partida la opción sera 1, en caso contrario se eligira la opción 2.
    """
    global matriz_jugador_1,matriz_jugador_2,jugador_1,jugador_2,turnos,messages_matriz,area_cada_boton
    if(opcion==2):
        archivo=open(f"Saves/{save.get()}.txt","w")
        archivo.write(f"Matriz_jugador_1:\n{ matriz_jugador_1}\nMatriz_jugador_2:\n{matriz_jugador_2}\nJugador_1:\n{jugador_1}\nJugador_2:\n{jugador_2}\nTurnos:\n{turnos}\nMessages_matriz:\n{messages_matriz}\nArea_cada_boton:\n{area_cada_boton}")
        ventana.destroy()
        aviso=tk.Toplevel()
        aviso.geometry("300x100+750+400")
        aviso.title("Guardado exitoso")
        aviso_label=tk.Label(aviso,text=f"El archivo {save.get()} fue guardado exitosamente,\n recuerda recordar el nombre del archivo.",font=("Times New Roman",11))
        aviso_label.pack(padx=10,pady=10)
    else:
        try:
            with open(f"Saves/{save.get()}.txt") as archivo:
                pe=-1
                save_objets=[[],[],[],[],[],[],[]]
                for e in archivo:
                    if(pe==-1):
                        match e:
                            case "Matriz_jugador_1:\n":
                                pe=0
                            case "Matriz_jugador_2:\n":
                                pe=1
                            case "Jugador_1:\n":
                                pe=2
                            case "Jugador_2:\n":
                                pe=3
                            case "Turnos:\n":
                                pe=4
                            case "Messages_matriz:\n":
                                pe=5
                            case "Area_cada_boton:\n":
                                pe=6
                    else:
                        save_objets[pe].append(eval(e))
                        pe=-1
                guardar_aqui(ma_1=save_objets[0][0],ma_2=save_objets[1][0],ju_1=save_objets[2][0],ju_2=save_objets[3][0],tu=save_objets[4][0],ms_matriz=save_objets[5][0],area=save_objets[6][0],new_game=False)
        except:
            error_label=tk.Label(ventana,text="Error: El archivo no existe.",font=("Times New Roman",12))
            error_label.place(x=20,y=110)

def tablas(interfaz_images:list):
    """Función que se encarga de establecer el ganador o si hubo tablas.

    Args:
        interfaz_images (list): Recibe las imagenes para la interfaz de victoria.
    """
    global jugador_2, jugador_1
    suma_1=0
    suma_2=0
    for e in jugador_1[3]:
        suma_1+=e
    for a in jugador_2[3]:
        suma_2+=a
    if(suma_1>suma_2):
        victoria(winner=jugador_1,losser=jugador_2,interfaz_images=interfaz_images)
    elif(suma_2>suma_1):
        victoria(winner=jugador_2,losser=jugador_1,interfaz_images=interfaz_images)
    else:
        victoria(winner=jugador_2,losser=jugador_1,interfaz_images=interfaz_images,tablas=True)

        

