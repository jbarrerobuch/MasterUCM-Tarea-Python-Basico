import subprocess
from random import randint
import time
from agente import algoritmos

class Agente():

    def __init__(self, nombre:str, dificultad:int, modelo:str= None, max_juegos:int=1):
        self.nombre = nombre # Nombre del agente
        self.dificultad = None # Dificultad del juego
        self.modelo = modelo # Modelo de la IA
        self.total_juegos = 0 # Contador de juegos realizados
        self.max_juegos = max_juegos # Núrmero máximo de juegos a jugar
        self.ultimo_numero = 0 # Último número seleccionado
        self.registro_intentos = []
        self.algoritmo = None

        # Comprobación de la dificultad
        assert dificultad in range(1, 4), "La dificultad debe ser un número entre 1 y 3."
        self.dificultad = dificultad

        if self.nombre == "Gemini":
            assert self.modelo is not None, "El modelo de la IA no puede ser None."
    
    def iniciar_juego(self):
        func = subprocess.Popen(
            ['python', 'main.py'], 
            stdin = subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            encoding='utf-8',
            )
        
        # Iniciar contador de intentos.
        numero_intento = 0

        while True:

            # Leer la linea del subproceso
            output = func.stdout.readline()

            # Romper el bucle is output es empty y subproceso ha terminado
            if output == '' and func.poll() is not None:
                break

            if output:

                # Print output
                print(f"[subprocess] {output.strip()}")

                # Selección de modo de juego
                if output == "¿Qué deseas hacer?: \n":

                    # Seleccionar modo solitario
                    if self.total_juegos >= self.max_juegos:
                        print("[Main] 4")
                        func.stdin.write("4\n")
                        func.stdin.flush()
                        break

                    print("[Main] 1")
                    func.stdin.write("1\n")
                    func.stdin.flush()
                    ultima_seleccion = True
                
                # Selección de dificultad
                elif output == "Introduce el nivel de dificultad: \n":
                    # Seleccionar dificultad Fácil
                    print("[Main] 1")
                    func.stdin.write("1\n")
                    func.stdin.flush()
                    #ultima_seleccion = "dificultad"
                
                # Captura del limite maximo del rango
                elif output.startswith("un número en estos momentos entre el 1 y el"):

                    self.limite_max_rango = int(output.strip().split(" ")[-1])
                    
                    # Inicialización de los algoritmos
                    if self.nombre == "Mitades":
                        self.algoritmo = algoritmos.mitades(limite_max_rango=self.limite_max_rango)
                    
                    elif self.nombre == "Gemini":
                        if self.modelo is None:
                            self.algoritmo = algoritmos.gemini(limite_max_rango=self.limite_max_rango)
                        else:
                            self.algoritmo = algoritmos.gemini(model=self.modelo, limite_max_rango=self.limite_max_rango)
                
                # Intento de acierto
                elif output == "Introduce un número: \n":
                    # Contabilizar intento
                    numero_intento += 1

                    # Seleccionar número segun el nombre del agente
                    if self.nombre == "Aleatorio":
                        numero = randint(1, self.limite_max_rango)

                    elif self.nombre == "Mitades" or self.nombre == "Gemini":
                        numero = int(self.algoritmo.seleccionar_numero().strip())

                    # Almacenar número
                    self.ultimo_numero = numero
                    print(f"[Main] {numero}")

                    # Enviar al subproceso
                    func.stdin.write(f"{numero}\n")
                    func.stdin.flush()
                
                elif output in ["El número secreto es mayor.\n", "El número secreto es menor.\n"]:
                    # Registro de respuesta
                    self.registro_intentos.append((self.ultimo_numero, output.strip()))

                    # Recibir indicación
                    if self.nombre == "Mitades":
                        self.algoritmo.eliminar_opciones(output)

                    if self.nombre == "Gemini":
                        self.algoritmo.agregar_respuesta(self.registro_intentos[-1])
                
                # Nombre para Estadísticas
                elif output == "Por favor Introduce tu nombre para almacenar las estadísticas de juego: \n":
                    # Introducir nombre
                    if self.nombre == "Gemini":
                        func.stdin.write(f"{self.modelo}\n")
                        print(f"[Main] {self.modelo}")
                    else:
                        print(f"[Main] {self.nombre}")
                        func.stdin.write(f"{self.nombre}\n")

                    func.stdin.flush()
                    self.total_juegos += 1
                    time.sleep(0.5)
        
        # Salir del bucle
        for i in range(2):
            output = func.stdout.readline()
            print(f"[subprocess] {output.strip()}")

                    

if __name__ == "__main__":
    agente = Agente(
        nombre="Gemini",
        modelo="gemini-1.5-flash",
        dificultad= 1,
        max_juegos=15
        )
    agente.iniciar_juego()