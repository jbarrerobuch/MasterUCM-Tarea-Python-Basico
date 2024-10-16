from .modo import solitario, dos_jugadores
from .estadistica import estadisticas
import os
import openpyxl
import datetime as dt

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

    # Selección del modo solitario
    if selección == 1:

        # Seleccionar numero intentos máximos
        max_intentos = seleccionar_dificultad()

        # Iniciar el juego en modo solitario
        resultado, intentos_usados = solitario(max_intentos=max_intentos)

        guardar_estadísticas(
            resultado = resultado,
            intentos_usados = intentos_usados,
            max_intentos = max_intentos,
            max_rango = 1000,
            modo_juego = "Solitario"
        )
    
    # Selección del modo 2 jugadores
    elif selección == 2:

        # Seleccionar numero intentos máximos
        max_intentos = seleccionar_dificultad()

        # Iniciar el juego en modo 2 jugadores
        resultado, intentos_usados = dos_jugadores(max_intentos=max_intentos)
        
        guardar_estadísticas(
            resultado = resultado,
            intentos_usados = intentos_usados,
            max_intentos = max_intentos,
            max_rango = 1000,
            modo_juego = "Dos jugadores"
        )

    elif selección == 3:
        estadisticas()

    elif selección == 4:
        print("¡Gracias por jugar!")
        print("Adios.")
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

def guardar_estadísticas(resultado:str, intentos_usados:int, max_intentos:int, max_rango:int, modo_juego:str):
    '''Guarda las estadisticas de juego en un archivo Excel.
    Se guardarán los datos requeridos en los argumentos:
    - Resultado (str): si el jugador adivinador es "ganador" o "perdedor".
    - Intentos_usados (int): intentos empleados por el jugador adivinador.
    - Max_intentos (int): número máximo de intentos permitidos.
    - Max_rango (int): número maximo del rango del número objetivo.

    Los datos se almacenarán junto con el nombre del jugador adivinador, la fecha y hora de la partida.
    '''
    nombre = input("Por favor Introduce tu nombre para almacenar las estadísticas de juego:\n")

    # Comprobar si existe el archivo de estadísticas
    if os.path.exists("estadisticas.xlsx"):

        # si existe, cargamos el archivo.
        archivo_excel = openpyxl.load_workbook("estadisticas.xlsx")

        # Comprobamos si el archivo contiene una pestaña llamada estadísticas
        if not "estadísticas" in archivo_excel.sheetnames:
            # Creramos la pestaña estadisticas si no existe y escribimos los nombres de las columnas.
            archivo_excel.create_sheet("estadísticas")
            pestaña = archivo_excel["estadísticas"]
            pestaña.append(["Nombre", "Timestamp", "Modo de Juego", "Resultado", "Intentos Usados", "Max Intentos", "Max Rango"])
        else:
            # Si la pestaña existe la seleccionamos.
            pestaña = archivo_excel["estadísticas"]
        

    else:
        # Si no existe, cargamos el archivos, creamos la pestaña estadísticas y escribimos los nombres de las columnas.
        archivo_excel = openpyxl.Workbook()
        archivo_excel.create_sheet("estadísticas")

        # Seleccionar la pestaña estadísticas
        pestaña = archivo_excel["estadísticas"]
        archivo_excel.active = pestaña
        pestaña.append(["Nombre", "Timestamp", "Modo de Juego", "Resultado", "Intentos Usados", "Max Intentos", "Max Rango"])

        # Borrar pestañas innecesarias
        lista_pestañas = archivo_excel.sheetnames
        lista_pestañas.remove("estadísticas")
        for pestaña_listada in lista_pestañas:
            archivo_excel.remove(worksheet=archivo_excel[pestaña_listada])

    # Escribimos los datos al final de los datos existentes y guardamos el archivo.
    pestaña.append([nombre, dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), modo_juego, resultado, intentos_usados, max_intentos, max_rango])
    archivo_excel.save("estadisticas.xlsx")


if __name__ == "__main__":
    datos = {
        "resultado": "Ganador",
        "intentos_usados": 5,
        "max_intentos": 20,
        "max_rango": 1000,
        "modo_juego": "Solitario"
    }
    guardar_estadísticas(**datos)