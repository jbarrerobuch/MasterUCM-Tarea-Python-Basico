from random import randint

def solitario(intentos:int)->bool:
    '''Juego en modo solitario. Es denecesario definir el número de intentos.
    La función devuelve:
    True si el jugador adivina el número o False si se le acaban los intentos.
    '''

    print("Has elegido jugar en modo solitario.")
    print("Te enfrentaras a la maquina que está eligiendo un numero en estos momentos.")
    objetivo = randint(1, 1000)
    objetivo = 500
    número_del_jugador = 0
    num_intentos = 0

    while num_intentos <= intentos:
        
        # Se muestra el intento actual
        print(f"Te quedan {intentos-num_intentos} intentos.")

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
                return True
    
    else:
        print("Oh que pena, te has quedado sin intentos.")
        print(f"has perdido. el número era {objetivo}")
        return False
