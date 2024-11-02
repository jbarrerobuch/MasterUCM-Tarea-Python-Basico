# Tarea para el módulo de Python básico  
  
## Descripción
  
Desarrollar un juego cuyo objetivo es adivinar un número (objetivo) entre el 1 y un límite máximo, en un número de intentos definido. Si el intento no acertado se indicará si el número objetivo es mayor o menor.  
  
El juego tiene modo de un jugador, dos jugadores y un módulo de estadísticas.  
  
Los modos de juego, el módulo de estadísticas como la opción de salir del juego se gestiona con un menú numérico mediante entrada de teclado, por el usuario.

#### Opciones del Menú  
1. Partida modo solitario  
2. Partida 2 Jugadores  
3. Estadística  
4. Salir  
  
Al finalizar el juego, se pide el nombre del jugador para almacenar las estadísticas en un documento de Excel y se vuelve siempre al menú inicial.

Tras la selección del modo de juego, se deberá elegir el nivel de dificultad mediante otro menú de entrada numérica.  
  
#### Niveles de dificultad  
El número de intentos se elige de forma aleatoria entre 1 y 20. Cada nivel de dificultad tiene asignado un rango de probabilidad de acierto, en base al cual se obtienen los límites máximos para delimitar el rango del número secreto. El límite máximo se escoge de forma aleatoria entre la probabilidad mínima y la máxima de cada nivel de dificultad.   
1. Fácil: rango probabilístico entre 50% y 5%  
2. Medio: rango probabilístico entre 5% y 0.2%  
3. Difícil: rango probabilístico entre 0.2% y 0.004%
4. Personalizado: el usuario elige numero de intentos como límite máximo del rango.  

## Descripción de las opciones
### Modo un jugador
  
El número objetivo será generado de forma aleatoria por el ordenador y el usuario deberá adivinarlo.  
  
### Modo dos jugadores  
  
El usuario 1 elegirá un número y el usuario 2 intentará adivinarlo.  
  
### Estadística  
  
El módulo de estadísticas de los datos guardados de cada juego. Consta de dos opciones:
1. Agrupados por Nombre de jugador.
2. Agrupados por nivel de dificultad.

Las funciones de agregado son comunes para ambos casos:
- Conteo de juegos: jugados, ganados y perdidos.
- Cálculos porcentuales de ganados y perdidos sobre el total de juegos.
- Calculo de promedio de intentos usados.
- Cálculo del promedio del porcentaje de intentos usados sobre el máximo de intentos en cada juego.
  
### Agente de juego

Desarrollado un agente que dispone de 3 algoritmos de juego.
- Aleatorio: acierta con escogiendo un número aleatorio dentro del rango de juego definiodo.
- Mitades: acierta con el numero central del rango descartando la mitad del rango segun la respuesta de salida del programa.
- Gemini: uso de la API de Google para interactuar con el LLM Gemini, modelo: gemini-1.5-flash. Es necesario definir la API KEY de Google desde el archivo “env.yml” dentro de la carpeta agente con el nombre “GOOGLE_API_KEY”. El uso del agente LLM necesita del módulo Langchain.
 
## Github
  
Todo el desarrollo ha sido documentado en Github: https://github.com/jbarrerobuch/Tarea-Python-Basico
