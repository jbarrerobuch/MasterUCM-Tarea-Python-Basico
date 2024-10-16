import pandas as pd

def estadisticas ():
    '''Lee y analiza el archivo de estadisticas y las imprime en la consola'''

    # Verifica si el archivo existe
    try:
        datos = pd.read_excel("estadisticas.xlsx")
    except FileNotFoundError:
        print("No existe o no se puede leer el achivo de estadisticas.")

    datos["Ganado"] = datos["Resultado"].apply(lambda x: 1 if x == "Ganador" else 0)
    datos["Perdido"] = datos["Resultado"].apply(lambda x: 1 if x == "Perdedor" else 0)
    datos["Total juegos"] = 1
    
    datos_jugador = datos.drop(columns=["Timestamp", "Resultado", "Modo de Juego"])
    
    datos_jugador = datos_jugador.groupby(["Nombre"], as_index=True).agg(
        {
            "Total juegos": "sum",
            "Ganado": "sum",
            "Perdido": "sum",
            "Intentos Usados": "mean",
            "Max Intentos": "mean",
            "Max Rango": "mean"
        }        
    )
    print()
    print(datos_jugador)

if __name__ == "__main__":
    estadisticas()