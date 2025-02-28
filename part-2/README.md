# Código

## Lógica del algoritmo

La estructura es la misma del BF implementado para la parte 1 del entregable, donde teníamos que encontrar el camino en una matriz simple. Los cambios realizados a este algoritmo están orientados a analizar si una casilla es accesible o no siendo vecina.

### `Node.py` - Función `set_neighbors`

```python
wall_coordinates = (coordinate_x + movement_x, coordinate_y + movement_y)
neighbor_coordinates = (coordinate_x + (movement_x * 2), coordinate_y + (movement_y * 2))
```

Como se ve arriba, tenemos dos variables porque la disposición de nuestra matriz tiene en cuenta tanto los espacios de las paredes como de los vecinos. Las casillas que están inmediatamente al lado son tomadas como secciones donde deberían ir paredes, y se toma la presencia o no de estas cuando hay un `#`. Por otro lado, los espacios a 2 de distancia representan los vecinos.

La validación que se hace para añadir una coordenada a los vecinos del nodo son:

1. El vecino esté dentro de los límites de la matriz.
2. Que la pared contigua a la casilla sea `' '`, `'S'` o `'E'`.

### `Node.py` - Función `set_neighbors`

```python
if 0 <= neighbor_coordinates[0] < len(maze) and 0 <= neighbor_coordinates[1] < len(maze[0]):
    if maze[wall_coordinates[1]][wall_coordinates[0]] in [' ', 'S', 'E']:
        self.neighbors.append((neighbor_coordinates, action_taken))
```

## Retos encontrados

- La disposición de la matriz puede enfrentar un reto de entendimiento porque se duplican la cantidad de casillas, y el análisis de movimiento refiere a ver las contiguas pero moverse a las que están más allá. Sin embargo, pudimos realizarlo ya que el profesor nos guió para llegar a dicha solución.

![robot-maze](https://github.com/user-attachments/assets/12d741a3-be70-4b2f-bf1c-156d15502746)

- Algo que sí fue imposible de lograr fueron los movimientos en Gazebo con ROS, puesto que la forma de renderización es muy inestable entre cada dispositivo.

## Posibles mejoras

- Por el alcance del proyecto, decidimos no implementar un `DistanceManager.py`, sino que solo usamos la distancia de Manhattan. Lo mismo aplica para múltiples salidas u obstáculos.

# Preguntas

### 1. ¿Qué desafíos surgen al trasladar la solución del algoritmo de búsqueda desde el código teórico a la práctica con el robot?

El desconocimiento sobre el programa ROS y Gazebo hizo imposible la programación del simulador. Sin embargo, desde lo que podemos intuir, un reto que dificultaría el paso del camino como lista a movimientos de un artefacto sería tener en cuenta hacia dónde queda mirando el robot después de cada movimiento. Por ejemplo, si el robot gira a la derecha, ahora todos los movimientos que haga hacia el frente harían que se desplace horizontalmente a la derecha.

Nuestra aproximación para que esto no ocurriera fue siempre hacer que el robot permanezca orientado al sur después de cada movimiento. Eso implica que para ir hacia adelante o atrás use velocidad lineal en el eje x, pero para ir a los costados haga un giro, se desplace y luego termine el giro (los 360 grados para que esté de nuevo mirando al sur).

### 2. ¿Cuál es la diferencia entre los algoritmos de búsqueda no informada como BFS (Breadth-First Search) y DFS (Depth-First Search) en este problema del laberinto?

Las dimensiones del laberinto son muy pequeñas, así que no se podría notar una diferencia en tiempo o memoria respecto a cada algoritmo. Sin embargo, para soluciones más grandes, BFS toma el liderazgo porque va priorizando varios frentes de búsqueda en vez de ir sin un patrón específico, lo que puede acelerar el descubrimiento de la salida.

### 3. ¿Cómo afecta el tamaño del laberinto a la eficiencia de BFS y DFS en términos de tiempo y espacio?

- **BFS**: En laberintos grandes, BFS tiende a consumir más memoria porque almacena todos los nodos en cada nivel del árbol de búsqueda. Sin embargo, garantiza encontrar la solución óptima (el camino más corto) en términos de número de pasos.
  
- **DFS**: En laberintos grandes, DFS puede ser más eficiente en términos de memoria, ya que solo almacena un camino a la vez. Sin embargo, no garantiza encontrar la solución óptima y puede tardar más tiempo en laberintos complejos debido a su naturaleza de profundidad.
