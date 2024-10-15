from .solitario import solitario

def inicializar_juego(primer_juego=True):

    if primer_juego:
        # Introducción
        print("Bienvenido al juego: Adivina el número")
        print("Instrucciones:")
        print("El juego consiste en adivinar un número ENTERO entre 1 y 1000")
        print("Después de cada intento, se te dará una pista: si el número a adivinar es mayor o menor a tu intento")
        print("Acontinuación, podrás elegir el modod de juego y la dificultad.")
        print("¡Buena suerte!")
    else:
        print()
        print("¡Bienvenido de nuevo!")
        print("Quieres intentarlo otra vez?")

    # Inicialización de la selección
    selección = 0

    while selección not in range(1, 5):
        print("Selecciona el modo de juego:")
        print("1. Partida modo solitario")
        print("2. Partida 2 Jugadores")
        print("3. Estadística")
        print("4. Salir")
        try:
            selección = int(input())
        except ValueError:
            print("Por favor, introduce un número válido.\n")
        else:
            if selección not in range(1, 5):
                print("Las opciones son del 1 al 4.\n")

    if selección == 1:
        número_de_intentos = seleccionar_dificultad()
        resultado = solitario(número_de_intentos)

        print("guardar stats")

    elif selección == 2:
        número_de_intentos = seleccionar_dificultad()
        print(f"selecionaste {selección}")
    elif selección == 3:
        print(f"selecionaste {selección}")
    elif selección == 4:
        print(f"selecionaste {selección}")
        print("Gracias por jugar")
        exit()
    
def seleccionar_dificultad()->int:
    '''Selecciona la dificultad del juego y devuelve el número de intentos
    de acuerdo a la dificultad seleccionada.'''
    dificultad = 0
    niveles = {
        1: 20,
        2: 12,
        3: 5
    }

    while dificultad not in range(1, 4):
        print("Selecciona la dificultad:")
        print("1. Fácil (20 intentos)")
        print("2. Medio (12 intentos)")
        print("3. Difícil (5 intentos)")

        try:
            dificultad = int(input())
        except ValueError:
            print("Por favor, introduce un número válido.\n")
        else:
            if dificultad not in range(1, 4):
                print("Las opciones son del 1 al 3.\n")
    return niveles[dificultad]