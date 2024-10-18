from random import randint
import getpass
from .puntos import calculo_puntos

def ronda_intentos(max_intentos:int, objetivo:int=None, limite_max_rango:int=1000):
    '''Rondas iterativas de intentos para adivinar el número objetivo.
    Si no se define numero objetivo, será generado aleatoriamente entre 1 y el rango 
    máximo definido. Valor por defect 1000.
    Requerido el número maximo de intentos para evaluar el resultado del juego.
    La función devuelve una tupla con:
    - resultado: "Ganador" si el jugador adivina el número o Perdedor si se le acaban los intentos.
    - intentos_usados: número de intentos consumidos por el usuario.'''

    # Si no se define un número objetivo se genera aleatoriamente, proceso para el modo un jugador.
    if objetivo is None:
        objetivo = randint(1, limite_max_rango)

    # Inicialización del contador de intentos usados
    intentos_usados = 0

    # Ronda iterativa de intentos hasta que se agoten los intentos o se adivine el número.
    while intentos_usados < max_intentos:
        
        # Se muestra el intento actual
        print(f"Te quedan {max_intentos-intentos_usados} intentos.")

        # Contablilizamos el intento
        intentos_usados += 1

        # Reiniciamos el número del jugador
        número_del_jugador = 0

        # El jugardor introduce un número valido
        while número_del_jugador not in range(1, limite_max_rango+1):
            try:
                número_del_jugador = int(input("Introduce un número: "))
            except ValueError:
                print(f"Por favor, sólo números ENTEROS válidos entre el 1 y {limite_max_rango}.\n")
            else:
                if número_del_jugador not in range(1, limite_max_rango+1):
                    print(f"Por favor, introduce un número válido entre 1 y {limite_max_rango}.\n")

        # Comprobamos el resultado
        else:
            if número_del_jugador < objetivo:
                print("El número secreto es mayor.\n")
            elif número_del_jugador > objetivo:
                print("El número secreto es menor.\n")
            else:
                if intentos_usados == 1:
                    print("Increible, has adivinado el número a la primera!!!")
                else:
                    print("Has adivinado el número!!!")
                    print(f"Solo has necesitado {intentos_usados} intentos.")

                puntos = calculo_puntos(intentos_usados=intentos_usados, max_rango=limite_max_rango)
                print(f"Has ganado {puntos} puntos.")
                print("=============================================\n")
                return ("Ganador", intentos_usados, puntos)
    
    else:
        print("Que pena, te has quedado sin intentos.")
        print(f"Has ganado 0 puntos.")
        print(f"has perdido. el número era {objetivo}")
        print("=============================================\n")
        return ("Perdedor", intentos_usados, 0)

def solitario(max_intentos:int, limite_max_rango:int=1000):
    '''Juego en modo solitario. Es necesario definir el número de intentos y el máximo del rango del
    número objetivo. Valor por defecto 1000.
    La función devuelve una tupla con:
    - resultado: "Ganador" si el jugador adivina el número o Perdedor si se le acaban los intentos.
    - intentos_usados: número de intentos consumidos por el usuario.
    '''
    print()
    print("=============================================")
    print("Has elegido jugar en modo solitario.")
    print(f"Te enfrentaras a la maquina que está eligiendo\n")
    print(f"un número en estos momentos entre el 1 y el {limite_max_rango}\n")
    
    return ronda_intentos(
        max_intentos=max_intentos,
        limite_max_rango=limite_max_rango
        )


def dos_jugadores(max_intentos:str, limite_max_rango:int=1000):
    '''Juego en modo 2 jugadores. Se requerirá al jugador 1 elegir un numero dentro
      de un rango entre 1 y un maximo variable, por defecto 1000. A continuación el
      jugador 2 deberá intentar adivinarlo.
      Es necesario definir el número de intentos.
      La función devuelve una tupla con:
      - resultado: "Ganador" si el jugador 2 adivina el número o Perdedor si se le acaban los intentos.
      - intentos_usados: número de intentos consumidos por el usuario.
      '''
    
    # Inicialización del juego
    print()
    print("=============================================")
    print("Has elegido el modo 2 jugadores.")
    print(f"El jugador 1 deberá elegir un numero entre el 1 y el {limite_max_rango}.")
    print(f"El jugador 2 tiene {max_intentos} intentos para adivinar el número.")

    # Jugador 1 elige el número objetivo
    objetivo = 0
    while objetivo not in range(1, limite_max_rango+1):
        try:
            objetivo = int(getpass.getpass(f"Jugador 1, por favor introduce un número entre 1 y {limite_max_rango}\n (Tu número está oculto, despues de escribirlo presiona enter): "))
        except ValueError:
            print("Por favor, introduce un número válido.\n")
        else:
            if objetivo not in range(1, limite_max_rango+1):
                print(f"El número debe estár entre 1 y {limite_max_rango}.\n")
    
    return ronda_intentos(
        max_intentos=max_intentos,
        objetivo=objetivo,
        limite_max_rango=limite_max_rango
        )
