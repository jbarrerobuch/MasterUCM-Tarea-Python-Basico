from .utilidades import *
from .modo import solitario, dos_jugadores
from .estadistica import estadisticas
from .dificultad import seleccionar_dificultad

import sys

def iniciar_juego(primer_juego=True):

    if primer_juego:
        # Introducción
        print("\nBienvenido al juego: Adivina el número")
        print("Instrucciones:")
        print("El juego consiste en adivinar un número ENTERO entre 1 y 1000")
        print("Después de cada intento, se te dará una pista: si el número a adivinar es mayor o menor a tu intento")
        print("A continuación, podrás elegir el modo de juego y la dificultad.")
        print("¡Buena suerte!")
    else:
        print("\n¡Bienvenido de nuevo!")
        print("Quieres intentarlo otra vez?")


    # Menú de principal
    menu_principal = {
        1: "Partida modo solitario",
        2: "Partida 2 Jugadores",
        3: "Estadística",
        4: "Salir"
    }

    selección = gestión_menu(menu_principal, msg_accion="¿Qué deseas hacer?: ")

    # Selección del modo solitario
    if selección == 1:

        print("Has elegido jugar en modo solitario.\n")

        # Seleccionar numero intentos máximos
        max_intentos, max_rango, dificultad = seleccionar_dificultad()

        print(f"Has seleccionado la dificultad: {dificultad}\n")

        # Iniciar el juego en modo solitario
        resultado, intentos_usados, puntos = solitario(max_intentos=max_intentos, limite_max_rango=max_rango)

        guardar_estadísticas(
            resultado = resultado,
            intentos_usados = intentos_usados,
            max_intentos = max_intentos,
            max_rango = max_rango,
            puntos = puntos,
            dificultad = dificultad,
            modo_juego = "Solitario"
        )
    
    # Selección del modo 2 jugadores
    elif selección == 2:

        # Seleccionar numero intentos máximos
        max_intentos, max_rango, dificultad = seleccionar_dificultad()

        # Iniciar el juego en modo 2 jugadores
        resultado, intentos_usados, puntos = dos_jugadores(max_intentos=max_intentos, limite_max_rango=max_rango)
        
        guardar_estadísticas(
            resultado = resultado,
            intentos_usados = intentos_usados,
            max_intentos = max_intentos,
            max_rango = max_rango,
            puntos = puntos,
            dificultad = dificultad,
            modo_juego = "Dos jugadores"
        )

    elif selección == 3:
        estadisticas()

    elif selección == 4:
        print("¡Gracias por jugar!")
        print("Adios.\n")
        sys.exit()