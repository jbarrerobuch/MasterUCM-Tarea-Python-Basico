import pandas as pd

def estadisticas ():
    '''Lee y analiza el archivo de estadisticas y las imprime en la consola'''

    print(f"Has seleccionado el análisis de estadísticas")

    # Verifica si el archivo existe
    try:
        datos = pd.read_excel("estadisticas.xlsx")
    except FileNotFoundError:

        print("No existe o no se puede leer el achivo de estadisticas.\n")
        return
        
    # Preparar los datos para los diferentes analisis
    datos["Ganados"] = datos["Resultado"].apply(lambda x: 1 if x == "Ganador" else 0)
    datos["Perdidos"] = datos["Resultado"].apply(lambda x: 1 if x == "Perdedor" else 0)
    datos["Jugados"] = 1
    datos["Porcentaje intentos"] = datos["Intentos Usados"] / datos["Max Intentos"] * 100

    # Definir la dificultad como categoría ordenada
    orden_dificultad = ["Personalizado", "Difícil", "Normal", "Fácil"]
    datos["Dificultad"] = pd.Categorical(datos["Dificultad"], categories=orden_dificultad, ordered=True)
    
    # Eliminar columns innecesarias
    datos = datos.drop(columns=["Timestamp", "Resultado", "Modo de Juego", "Max Intentos", "Max Rango"])

    while True:
        ### Menu para diferentes estadisticas###
        selección = 0
        while selección not in range(1, 4):
            print("Selecciona el tipo de estadística que deseas ver:")
            print("1. Estadísticas generales por Jugador")
            print("2. Estadísticas por dificultad")
            print("3. Salir")
            try:
                selección = int(input())
            except ValueError:
                print("Por favor, introduce un número válido.\n")
            else:
                if selección not in range(1, 4):
                    print("Las opciones son del 1 al 3.\n")
        

        if selección == 3: # Salir
            print()
            break

        else:
                
            if selección == 1: # Estadísticas generales por Jugador y dificultad
                
                # duplicado de datos para transformación
                datos_transformados = datos.copy()

                # Agrupar los datos por Nombre de jugador con diferentes agregados para cada dato.
                datos_transformados = datos_transformados.groupby(["Dificultad", "Nombre"], observed=False, as_index=True).agg(
                    {
                        "Jugados": "sum",
                        "Ganados": "sum",
                        "Perdidos": "sum",
                        "Intentos Usados": promedio_redondeado,
                        "Porcentaje intentos": lambda x: promedio_redondeado(x, decimales=1),
                        "Puntos": "sum"
                    }
                )
                
                # Renombrado de columnas y reordenamiento
                datos_transformados["Promedio intentos"] = datos_transformados["Intentos Usados"]
                datos_transformados = datos_transformados.drop(columns=["Intentos Usados"])
                datos_transformados =datos_transformados.reindex(columns=["Jugados", "Ganados", "Perdidos", "Puntos", "Promedio intentos", "Porcentaje Ganados", "Porcentaje Perdidos", "Porcentaje intentos"])
                datos_transformados = datos_transformados.sort_values(by=["Dificultad","Puntos"], ascending=False)
                
                # Calculo de otros datos porcentuales
                datos_transformados["Porcentaje Ganados"] = round(datos_transformados["Ganados"] / datos_transformados["Jugados"] * 100,1)
                datos_transformados["Porcentaje Perdidos"] = round(datos_transformados["Perdidos"] / datos_transformados["Jugados"] * 100,1)
                datos_transformados = datos_transformados.fillna(0)
                
                # Imprimir los datos
                print()
                print("========Datos nominales agregados por jugador========")
                print(datos_transformados[["Jugados", "Ganados", "Perdidos", "Puntos", "Promedio intentos"]])
                print()
                print("========Datos porcentuales agregados por jugador========")
                print(datos_transformados[["Porcentaje Ganados", "Porcentaje Perdidos", "Porcentaje intentos"]])
                print()

            elif selección == 2: # Estadísticas por dificultad

                datos_transformados = datos.copy()
                # Eliminar columns innecesarias
                datos_transformados["Promedio Puntos"] = datos_transformados["Puntos"]
                datos_transformados = datos_transformados.drop(columns=["Nombre", "Puntos"])

                # Agrupar los datos por Nombre de jugador con diferentes agregados para cada dato.
                datos_transformados = datos_transformados.groupby(["Dificultad"], as_index=True).agg(
                    {
                        "Jugados": "sum",
                        "Ganados": "sum",
                        "Perdidos": "sum",
                        "Intentos Usados": "mean",
                        "Porcentaje intentos": "mean",
                        "Promedio Puntos": "mean"
                    }
                )

                # Calculo de otros datos porcentuales
                datos_transformados["Porcentaje Ganados"] = round(datos_transformados["Ganados"] / datos_transformados["Jugados"] * 100,1)
                datos_transformados["Porcentaje Perdidos"] = round(datos_transformados["Perdidos"] / datos_transformados["Jugados"] * 100,1)

                # Renombrados de columna y reordenamiento
                datos_transformados =datos_transformados.reindex(columns=["Jugados", "Ganados", "Perdidos", "Promedio Puntos", "Promedio intentos", "Porcentaje Ganados", "Porcentaje Perdidos", "Porcentaje intentos"])
                datos_transformados = datos_transformados.sort_values(by=["Dificultad"], ascending=False)

                # Filtrar los datos NaN
                datos_transformados = datos_transformados.fillna(0)
                    
                # Imprimir los datos
                print()
                print("========Datos nominales agregados por dificultad========")
                print(datos_transformados[["Jugados", "Ganados", "Perdidos", "Promedio Puntos", "Promedio intentos"]])
                print()
                print("========Datos porcentuales agregados por dificultad========")
                print(datos_transformados[["Porcentaje Ganados", "Porcentaje Perdidos", "Porcentaje intentos"]])
                print()


def promedio_redondeado(series, decimales=0):
    return int(series.mean().round(decimales))

if __name__ == "__main__":
    estadisticas()