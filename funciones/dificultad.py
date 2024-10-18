from random import randint

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
    '''Selecciona la dificultad del juego y devuelve el número de intentos  
    y el rango maximo de numeros de acuerdo a la dificultad seleccionada.'''
    dificultad_int = 0
    niveles = {
        1: [0.5, 0.05, "Fácil"],
        2: [0.05, 0.0002, "Normal"],
        3: [0.0002, 0.00004, "Difícil"],
        4: [0, 0, "Personalizado"]
    }

    while dificultad_int not in niveles.keys():
        print("El número de intentos se selecciona aleatoriamente entre 1 y 20.")
        print("El rango de números enteros se calcula en base a la dificultad seleccionada.\n")
        print("Selecciona la dificultad:")
        print("1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print("4. Personalizado - té decides número de intentos y el rango\n")
        print("Segun la dificultad y el numero de aciertos usados se calularan los puntos para el ranking\n")

        try:
            dificultad_int = int(input("Introduce el número de la dificultad: "))
        except ValueError:
            print("\nPor favor, introduce un número válido.\n")
        else:
            if dificultad_int not in niveles.keys():
                print(f"\nLas opciones son del 1 al {len(niveles)}.\n")
    
    if dificultad_int == 4:
        max_intentos = None
        limite_max_rango = None
        dificultad = "Personalizado"

        while max_intentos == None or limite_max_rango == None or max_intentos >= limite_max_rango:
            try:
                max_intentos = int(input("Introduce el número de intentos: "))
                limite_max_rango = int(input("Introduce el rango máximo de números enteros: "))
            except ValueError:
                print("Por favor, introduce un número válido.\n")
            else:
                if max_intentos >= limite_max_rango:
                    print("El número de intentos debe ser menor que el rango de números enteros.\n")

    else:
        max_prob, min_prob, dificultad = niveles[dificultad_int]

        max_intentos = randint(1, 20)
        limite_rango_max_prob = calculo_rango(probabilidad=max_prob, num_intentos=max_intentos)
        limite_rango_min_prob = calculo_rango(probabilidad=min_prob, num_intentos=max_intentos)

        try:
            limite_max_rango = randint(limite_rango_max_prob, limite_rango_min_prob)
        except ValueError:
            limite_max_rango = randint(limite_rango_min_prob, limite_rango_max_prob)
        
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

