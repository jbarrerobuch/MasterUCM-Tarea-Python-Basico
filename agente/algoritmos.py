from langchain_google_genai import ChatGoogleGenerativeAI
import yaml
import os

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

class gemini_sin_memoria():
    def __init__(self,
                 model:str="gemini-1.5-flash",
                 limite_max_rango = 0
                 ) -> None:
        
        self.model = model
        self.limite_max_rango = limite_max_rango
        # Cargar API key a variable de entorno
        with open("agente/env.yml", "r") as file:
            os.environ["GOOGGLE_API_KEY"] = yaml.safe_load(file)["GOOGLE_API_KEY"]
        print()
        print("API:", os.environ["GOOGGLE_API_KEY"])

        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            api_key=os.environ["GOOGGLE_API_KEY"])

    def enviar_mensaje(self, mensaje:str):
        mensaje = [
            (
                "system",
                f"Estamos jugando que adivines un numero secreto entre el 1 y el {self.limite_max_rango}"
            ),
            (
                "human",
                mensaje
            )
        ]
        respuesta = self.llm.invoke(mensaje)
        return respuesta

if __name__ == "__main__":
    agente = gemini_sin_memoria()
    print(agente.enviar_mensaje("Recuerda esto: Tanto monta, monta tanto, Isabel como Fernando."))
    print(agente.enviar_mensaje("¿Que te he peido que recuerdes?"))
