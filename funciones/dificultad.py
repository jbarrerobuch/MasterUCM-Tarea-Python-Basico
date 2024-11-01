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

    return int(round((1 / probabilidad) + num_intentos,0))


def seleccionar_dificultad():
    '''Seleccion de la dificultad del juego. Devuelve el número de intentos  
    y el rango maximo de números de acuerdo a la dificultad seleccionada.'''

    selección_dificultad = 0
    niveles = {
        1: [0.5, 0.05, "Fácil"],
        2: [0.05, 0.0002, "Normal"],
        3: [0.0002, 0.00004, "Difícil"],
        4: [0, 0, "Personalizado"]
    }

    while selección_dificultad not in niveles.keys():

        print("El número de intentos se selecciona aleatoriamente entre 1 y 20.")
        print("El rango de números enteros se calcula en base a la dificultad seleccionada.\n")
        print("i deseas elegir ambos parametros de juego, selecciona la opción de juego personalizado 4.\n")
        print("Selecciona la dificultad:")
        print("1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print("4. Personalizado")
        print("Segun la dificultad y el numero de aciertos usados se calularan los puntos para el ranking\n")
        print("Introduce el nivel de dificultad: ")
        selección_dificultad = utilidades.validar_selección(input(), opción_max=4)
        
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


if __name__ == "__main__":
    vals = [
        (0.6, 5),
        (0.4, 5),
        (0.2, 5),
        (0.1, 5),
        (0.05, 5)
    ]
    print()
    for i in vals:
        prob, intentos = i
        max_rango = calculo_rango(probabilidad=prob, num_intentos=intentos)
        probabilidad = probabilidades(num_intentos=intentos, max_rango=max_rango)
        print(f"{i} - {max_rango} - {probabilidad}")

