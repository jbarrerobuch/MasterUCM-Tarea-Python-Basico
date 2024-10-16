# Tarea para el módulo de Python básico  
  
## Descripción
  
Desarrollar un juego que cosiste en adiviniar un número (objetivo) del 1 al 1000, en un cantidad  
de intentos definido por la dificultad escogida. Si el intento es fallido se indicará como pista  
si el número propuesto es mayor o menor que el número objetivo.  
  
El juego tendrá modo de un jugador, dos jugadores y un modulo de estadisticas.  
  
Los modos de juego, el modulo de estadisticas como la opción de salir del juego se gestionará con un menú numérico mediante entrada de teclado, por el usuario.

#### Opciones del Menú  
1. Partida modo solitario  
2. Partida 2 Jugadores  
3. Estadística  
4. Salir  
  
Al finalizar el juego, se pedirá el nombre del jugador para almacenar las estadisticas en un documento de Excel y se volverá siempre al menu inicial.

Tras la selección del modo de juego, se deberá elegir el nivel de dificultad mediante un menu de entrada numérica.

#### Niveles de dificultad  
1. Fácil (20 intentos)  
2. Medio (12 intentos)  
3. Difícil (5 intentos)  

## Descripción de las opciones
### Modo un jugador
  
El número objetivo será generado de forma aleatoria por el ordenador y el usuario deberá adivinarlo.  
  
### Modo dos jugadores  
  
El usuario 1 elegirá un número y el usuario 2 intentará adivinarlo.  
  
### Estadística  
  
El módulo de estadísticas de los datos guardados de cada juego. Consta de dos opciones:
1. Agrupados por Nombre de jugador.
2. Agrupados por nivel de difcultad.

Las funciones de agregado son comunes para ambos casos:
- Conteo de juegos: jugados, ganados y perdidos.
- Calculos porcentuales de ganados y perdidos sobre el total de juegos.
- Calculo de promedio de intentos usados.
- Calculos del promedio de porcentaje de intentos usados sobre el maximo de intentos en cada juego.