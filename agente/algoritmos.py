from langchain_google_genai import ChatGoogleGenerativeAI
from google.api_core.exceptions import ResourceExhausted
import time
from datetime import datetime as dt
import yaml
import pprint
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

class gemini():
    def __init__(self,
                 model:str="gemini-1.5-flash",
                 limite_max_rango = 0
                 ) -> None:
        
        self.model = model
        self.limite_max_rango = limite_max_rango
        self.respuestas = []
        self.usage_metadata = {
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "requests_min": 0,
            "timer": None
        }

        # Cargar API key a variable de entorno
        with open("agente/env.yml", "r") as file:
            os.environ["GOOGGLE_API_KEY"] = yaml.safe_load(file)["GOOGLE_API_KEY"]

        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            api_key=os.environ["GOOGGLE_API_KEY"],
            temperature=0
            )
            
    def agregar_respuesta(self, respuesta:tuple):
        numero, pista = respuesta
        self.respuestas.append(f"{numero}:{pista}")
        

    def seleccionar_numero(self) -> str:

        # Mensaje para primer intento
        if len(self.respuestas) == 0:
            system_msg =(
                "system",
                f"Estamos jugando a que adivines un numero secreto entre el 1 y el {self.limite_max_rango}.\
                Tras cada intento de acierto te diré si el número secreto es mayor o menor a tu número.\
                Es tu primer intento. Responde solo el número que crees que es el secreto en caracteres numericos."
            )
        
        # Mensaje para intentos posteriores
        else:
            system_msg = (
                "system",
                f"""Estamos jugando a que adivines un numero secreto entre el 1 y el {self.limite_max_rango}.
                Tras cada intento de acierto te diré si el número secreto es mayor o menor a tu número.
                Te voy a decir que numeros has usado de momento con el formato 'numero:respuesta'.\n
                {','.join(self.respuestas)}\n\
                Responde solo el número que crees que es el secreto en caracteres numericos."""
            )

        human_msg = (
            "human",
            "¿Cual es el número secreto?"
        )

        mensaje = [system_msg,human_msg]

        if not self.usage_metadata["timer"] is None:

            # Comprabar uso de la API y esperar si es necesartio
            while self.usage_metadata["requests_min"] >= 11 and (dt.now() - self.usage_metadata["timer"]).seconds < 60:
                pause = 60 - (dt.now() - self.usage_metadata["timer"]).seconds
                print(f"Se ha excedido el límite de uso de la API, esperando {pause} segundos para reintentar")
                pprint.pprint(self.usage_metadata)
                time.sleep(pause)
        

        try:
            respuesta = self.llm.invoke(mensaje)

        except ResourceExhausted:
            print("Se ha excedido el límite de uso de la API, esperando 1 minuto para reintentar")
            time.sleep(60)
            respuesta = self.llm.invoke(mensaje)
        finally:
            if self.usage_metadata["timer"] is None or (dt.now() - self.usage_metadata["timer"]).seconds >= 60:
                self.usage_metadata["timer"] = dt.now()
                self.usage_metadata["requests_min"] = 0
            else:
                self.usage_metadata["requests_min"] += 1

        # Contabilizar uso de la API
        usage = respuesta.usage_metadata
        for key, value in usage.items():
            self.usage_metadata[key] += value
        return respuesta.content

if __name__ == "__main__":
    agente = gemini()
    for i in range(18):
        print(agente.seleccionar_numero())
