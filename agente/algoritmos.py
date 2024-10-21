


class mitades():
    def __init__(self, limite_max_rango:int) -> None:
        self.opciones = [i for i in range(1, limite_max_rango+1)]
        self.ultma_seleccion = None
    
    def seleccionar_numero(self):
        self.ultma_seleccion = self.opciones[(len(self.opciones)//2)-1]
        return self.ultma_seleccion
    
    def eliminar_opciones(self, indicacion:str):
        if indicacion == "El número secreto es mayor.\n":
            self.opciones = self.opciones[len(self.opciones)//2:]
        elif indicacion == "El número secreto es menor.\n":
            self.opciones = self.opciones[:len(self.opciones)//2]

class llm():
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    agente = mitades(limite_max_rango=1000)
    num_secreto = 850
    while True:
        print(agente.seleccionar_numero())
        if agente.ultma_seleccion < num_secreto:
            agente.eliminar_opciones("El número secreto es mayor.\n")
        elif agente.ultma_seleccion > num_secreto:
            agente.eliminar_opciones("El número secreto es menor.\n")
        else:
            print("Has adivinado el número!!!")
            break
        print(f"opcion min: {agente.opciones[0]} - opcion max: {agente.opciones[-1]}")
