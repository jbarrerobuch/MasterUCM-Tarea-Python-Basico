import pandas as pd

def estadisticas ():
    '''Lee y analiza el archivo de estadisticas y las imprime en la consola'''

    print(f"Has seleccionado el análisis de estadísticas")

    # Verifica si el archivo existe
    try:
        datos = pd.read_excel("estadisticas.xlsx")
    except FileNotFoundError:
        datos = pd.DataFrame()
        print("No existe o no se puede leer el achivo de estadisticas.")

    while not datos.empty:
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
        
            datos["Ganados"] = datos["Resultado"].apply(lambda x: 1 if x == "Ganador" else 0)
            datos["Perdidos"] = datos["Resultado"].apply(lambda x: 1 if x == "Perdedor" else 0)
            datos["Jugados"] = 1
            datos["Porcentaje intentos"] = round(datos["Intentos Usados"] / datos["Max Intentos"] * 100,0)

        if selección == 3: # Salir
            print()
            break

        else:
            if selección == 1: # Estadísticas generales por Jugador

                datos_transformados = datos
                # Eliminar columns innecesarias
                datos_transformados = datos_transformados.drop(columns=["Timestamp", "Resultado", "Modo de Juego", "Max Intentos", "Max Rango"])
                
                # Agrupar los datos por Nombre de jugador con diferentes agregados para cada dato.
                datos_transformados = datos_transformados.groupby(["Nombre"], as_index=True).agg(
                    {
                        "Jugados": "sum",
                        "Ganados": "sum",
                        "Perdidos": "sum",
                        "Intentos Usados": "mean",
                        "Porcentaje intentos": "mean"
                    }
                )

            elif selección == 2: # Estadísticas por dificultad

                datos_transformados = datos
                # Eliminar columns innecesarias
                datos_transformados = datos_transformados.drop(columns=["Timestamp", "Resultado", "Nombre"])

                # Agrupar los datos por Nombre de jugador con diferentes agregados para cada dato.
                datos_transformados = datos_transformados.groupby(["Max Intentos"], as_index=True).agg(
                    {
                        "Jugados": "sum",
                        "Ganados": "sum",
                        "Perdidos": "sum",
                        "Intentos Usados": "mean",
                        "Porcentaje intentos": "mean"
                    }
                )

            # Calculo de otros datos porcentuales
            datos_transformados["Porcentaje Ganados"] = datos_transformados["Ganados"] / datos_transformados["Jugados"] * 100
            datos_transformados["Porcentaje Perdidos"] = datos_transformados["Perdidos"] / datos_transformados["Jugados"] * 100

            # Renombrados de columna y reordenamiento
            datos_transformados["Promedio intentos"] = datos_transformados["Intentos Usados"]
            datos_transformados = datos_transformados.drop(columns=["Intentos Usados"])
            datos_transformados =datos_transformados.reindex(columns=["Jugados", "Ganados", "Perdidos", "Promedio intentos", "Porcentaje Ganados", "Porcentaje Perdidos", "Porcentaje intentos"])
            
            # Impresión de los datos
            print()
            print(datos_transformados)


if __name__ == "__main__":
    estadisticas()