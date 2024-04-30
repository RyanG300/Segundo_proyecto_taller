from PIL import ImageTk, Image
import logica as log

def solo_numeros(caracter):
    """Verifica si 'caracter' es un número

    Args:
        caracter (_type_): Caracter a verificar.

    Returns:
        _type_: True si 'caracter' es un número, de lo contrario retorna False.
    """
    return caracter.isdigit()

def validar_input(P):
    """Valida si el caracter es un número o está vacío

    Args:
        P (_type_): Caracter a validar

    Returns:
        _type_: True si P es un número entero o está vacío, de lo contrario retorna False.
    """
    if solo_numeros(P) or P == "":
        return True
    else:
        return False

def call(ventana):
   return ventana.register(validar_input)

def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):
    """Centra la ventana en la pantalla utilizando las dimensiones proporcionadas.

    Args:
        ventana (_type_): La ventana a centrar
        aplicacion_ancho (_type_): Ancho deseado para la ventana.
        aplicacion_largo (_type_): Largo deseado para la ventana.

    Returns:
        _type_: Ventana centrada
    """
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (aplicacion_ancho/2))
    y = int((pantalla_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
