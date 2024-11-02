from random import randint
from . import utilidades

__all__ = ["probabilidades", "calculo_rango", "seleccionar_dificultad"]

def probabilidades(num_intentos:int, max_rango:int) -> float:
    '''Calcula la probabilidad de adivinar un número en un rango determinado  
    de numeros enteros. Tras cada intento se reduce en numero de opciones  
    aumentando las probabilidades.  
    Args:
        - num_intentos (int) : Numero de intentos.  
        - max_rango (int) : Rango de numeros enteros.  

    -----
    Return:  
    1 / (max_rango - num_intentos)
    '''

    return 1 / (max_rango - (num_intentos - 1))


def calculo_rango(probabilidad:float, num_intentos:int) -> int:
    '''Calcula el limitime superior del rango de números enteros dada una probailidad y un numero de intentos.
    Args:
        - probabilidad (float) : Probabilidad maima de adivinar un número en un rango de números enteros.
        - num_intentos (int) : Número de intentos.'''

    return int(round((1 / probabilidad) + num_intentos,0))


def seleccionar_dificultad():
    '''Seleccion de la dificultad del juego. Devuelve el número de intentos  
    y el rango maximo de números de acuerdo a la dificultad seleccionada.'''

    niveles = {
        1: [0.5, 0.05, "Fácil"],
        2: [0.05, 0.0002, "Normal"],
        3: [0.0002, 0.00004, "Difícil"],
        4: [0, 0, "Personalizado"]
    }

    menu_dificultad = {
        1: "Fácil",
        2: "Normal",
        3: "Difícil",
        4: "Personalizado"
    }

    print("El número de intentos se selecciona aleatoriamente entre 1 y 20.")
    print("El rango de números enteros se calcula en base a la dificultad seleccionada.\n")
    print("Si deseas elegir ambos parametros de juego, selecciona la opción de juego personalizado 4.\n")
    print("Segun la dificultad y el numero de aciertos usados se calularan los puntos para el ranking\n")

    selección_dificultad = utilidades.gestión_menu(
        menu_dificultad,
        msg_intro="Estos son los niveles de dificultad:",
        msg_accion="¿Qué nivel de dificultad eliges?: ")
        
    if selección_dificultad == 4:
        max_intentos = None
        limite_max_rango = None
        dificultad = "Personalizado"

        while max_intentos == None or limite_max_rango == None or max_intentos >= limite_max_rango:
            try:
                max_intentos = int(input("Introduce el número de intentos: "))
                limite_max_rango = int(input("Introduce el rango máximo de números enteros: "))
            except ValueError:
                print("Por favor, introduce un número entero válido para intentos y limite maximo.\n")
            else:
                if max_intentos >= limite_max_rango:
                    print("El número de intentos debe ser menor que el rango de números enteros.\n")

    else:
        probabilidad_maxima, probabilidad_minima, dificultad = niveles[selección_dificultad]

        max_intentos = randint(1, 20)
        limite_rango_bajo = calculo_rango(probabilidad=probabilidad_maxima, num_intentos=max_intentos)
        limite_rango_alto = calculo_rango(probabilidad=probabilidad_minima, num_intentos=max_intentos)

        # Con rangos muy ajustados de probabilidades, los valores para el limite de rango podrian invertirse.
        try:
            limite_max_rango = randint(limite_rango_bajo, limite_rango_alto)
        except ValueError:
            limite_max_rango = randint(limite_rango_alto, limite_rango_bajo)
        
    return max_intentos, limite_max_rango, dificultad
