import subprocess
from random import randint
import time
from agente import algoritmos

class Agente():

    def __init__(self, nombre:str, dificultad:int, max_juegos:int=1):
        self.nombre = nombre # Nombre del agente
        self.dificultad = None # Dificultad del juego
        self.total_juegos = 0 # Contador de juegos realizados
        self.max_juegos = max_juegos # Núrmero máximo de juegos a jugar
        self.registro_intentos = {}

        # Comprobación de la dificultad
        assert dificultad in range(1, 4), "La dificultad debe ser un número entre 1 y 3."
        self.dificultad = dificultad
    
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
        intento_numero = 0

        while True:
            output = func.stdout.readline()
            if output == '' and func.poll() is not None:
                break

            if output:
                #if ultima_seleccion == "dificultad":
                #    self.max_intentos, self.limite_max_rango, self.dificultad = tuple(output.strip())
                #    ultima_seleccion = False
                #
                #else:
                    print(f"[subprocess] {output.strip()}")

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
                    
                    elif output == "Introduce el nivel de dificultad: \n":
                        # Seleccionar dificultad Fácil
                        print("[Main] 1")
                        func.stdin.write("1\n")
                        func.stdin.flush()
                        #ultima_seleccion = "dificultad"
                    
                    elif output.startswith("un número en estos momentos entre el 1 y el"):
                        # Seleccionar rango maximo
                        self.limite_max_rango = int(output.strip().split(" ")[-1])
                        
                        # Inicialización de los algoritmos
                        if self.nombre == "Mitades":
                            self.algoritmo = algoritmos.mitades(limite_max_rango=self.limite_max_rango)
                    
                    # Intento de acierto
                    elif output == "Introduce un número: \n":
                        # Contabilizar intento
                        intento_numero += 1

                        # Seleccionar número segun el nombre del agente
                        if self.nombre == "Aleatorio":
                            numero = randint(1, self.limite_max_rango)
                        elif self.nombre == "Mitades":
                            numero = self.algoritmo.seleccionar_numero()
                        elif self.nombre == "Gemini":
                            pass

                        # Almacenar número
                        self.registro_intentos[intento_numero] = numero
                        print(f"[Main] {numero}")

                        # Enviar al subproceso
                        func.stdin.write(f"{numero}\n")
                        func.stdin.flush()
                    
                    elif output in ["El número secreto es mayor.\n", "El número secreto es menor.\n"]:
                        # Recibir indicación
                        if self.nombre == "Mitades":
                            self.algoritmo.eliminar_opciones(output)
                    
                    # Nombre para Estadísticas
                    elif output == "Por favor Introduce tu nombre para almacenar las estadísticas de juego: \n":
                        # Introducir nombre
                        print(f"[Main] {self.nombre}")
                        func.stdin.write(f"{self.nombre}\n")
                        func.stdin.flush()
                        self.total_juegos += 1
                        time.sleep(0.1)
        
        # Salir del bucle
        for i in range(2):
            output = func.stdout.readline()
            print(f"[subprocess] {output.strip()}")

                    

if __name__ == "__main__":
    agente = Agente(
        nombre="Mitades",
        dificultad= 1,
        max_juegos=1
        )
    agente.iniciar_juego()