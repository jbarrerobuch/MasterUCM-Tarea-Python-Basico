import math

def probabilidades(num_intentos:int, max_rango:int) -> float:
    '''Calcula la probabilidad promedio de adivinar un número en un rango en un numero limitado de intentos.'''
    # Convert input strings to integers
    num_intentos = num_intentos
    max_rango = max_rango
    
    # Initialize sum of cumulative probabilities
    probabilidades = []
    
    # Loop through the number of attempts
    for intento in range(1, num_intentos + 1):

        # Calculate the cumulative probability of guessing correctly at least once
        numeros_restantes = max_rango - (intento - 1)
        probabilidad = 1 - (1 - 1 / numeros_restantes)
        print(f"Probabilidad de adivinar en el intento {intento}: {probabilidad}")
        # Sum the cumulative probabilities
        probabilidades.append(probabilidad)
    
    return max(probabilidades)


if __name__ == "__main__":
    resultado = probabilidades(5, 10)
    print(f"Resultado: {resultado}")
