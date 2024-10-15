from random import randint

def dos_jugadores(max_intentos:str):
    '''Juego en modo 2 jugadores. Se requerirá al jugador 1 elegir un numero dentro
      del rango 1 a 1000. A continuación el jugador 2 deberá intentar adivinar.
      Es necesario definir el número de intentos.
      La función devuelve una tupla con:
      - resultado: "Ganador" si el jugador 2 adivina el número o Perdedor si se le acaban los intentos.
      - intentos_usados: número de intentos consumidos por el usuario.
      '''
    
    # Inicialización del juego
    print("Has elegido el modo 2 jugadores.")
    print("El jugador 1 deberá elegir un numero entre el 1 y el 1000.")
    print("El jugador 2 deberá adivinar el número antes de quedarse sin intentos.")
    objetivo = randint(1, 1000)
    número_del_jugador = 0
    num_intentos = 0

    # Jugador 1 elige el número objetivo
    objetivo = int(input("Jugador 1, por favor introduce un número: "))

    # Ronda de intentos de acierto
    while num_intentos <= max_intentos:
        # Se muestra el intento actual
        print(f"Te quedan {max_intentos-num_intentos} intentos.")

        # Contablilizamos el intento
        num_intentos += 1

        # Reiniciamos el número del jugador
        número_del_jugador = 0

        # El jugardor introduce un número valido
        while número_del_jugador not in range(1, 1001):
            try:
                número_del_jugador = int(input("Introduce un número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
            else:
                if número_del_jugador not in range(1, 1001):
                    print("El número objetivo está entre 1 y 1000.\n")

        # Comprobamos el resultado
        else:
            if número_del_jugador < objetivo:
                print("Tu número es menor.")
            elif número_del_jugador > objetivo:
                print("Tu numero es mayor.")
            else:
                print("Increible, has adivinado el número!!!")
                print(f"Solo has necesitado {num_intentos} intentos.")
                return ("Ganador", num_intentos)
    
    else:
        print("Oh que pena, te has quedado sin intentos.")
        print(f"has perdido. el número era {objetivo}")
        return ("Perdedor", num_intentos)

