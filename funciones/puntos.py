from .dificultad import probabilidades

__all__ = ["calculo_puntos"]

def calculo_puntos(intentos_usados:int, max_rango:int) -> int:
    '''Calcula los puntos obtenidos en una partida en función de probabilidad de fracaso al inicio del juego  
    y en el intento acertado multiplicado por 100'''
    probabilidad_fracaso_primer_intento = 1 - probabilidades(num_intentos=1, max_rango=max_rango)
    probabilidades_fracaso_intentos_usados = 1 - probabilidades(num_intentos=intentos_usados, max_rango=max_rango)
    return int(round( (probabilidad_fracaso_primer_intento + probabilidades_fracaso_intentos_usados) * 100, 0))