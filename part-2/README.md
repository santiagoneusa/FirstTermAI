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

El desconocimiento sobre Ros y Gazebo marcó un obstáculo fuerte porque no conocíamos la tecnología. No entender cómo funcionaba el módullo por debajo pero tener que programar la simulación era complejo.

Relacionado con el aspecto anterior, encontramos que era complejo mantener los movimientos y rotaciones del robot porque cada uno de los movimientos comprendían un cambio de perspectiva constante. De esta forma fue necesario implementar un formateador de acciones poniéndose en la perspectiva del robot en todo momento.

### `Node.py` - Función `reconstruct_path`

```python
path_actions_taken = []
node = self

while node.parent is not None:
    path_actions_taken.insert(0, node.action_taken)
    node = node.parent

looking_at = initial_looking_at
formated_path = []
for direction in path_actions_taken:
    if direction == 'north': # ...
    elif direction == 'south': # ...
    elif direction == 'west': # ...
    elif direction == 'east': # ...
return formated_path
```

### 2. ¿Cuál es la diferencia entre los algoritmos de búsqueda no informada como BFS (Breadth-First Search) y DFS (Depth-First Search) en este problema del laberinto?

Las dimensiones del laberinto son muy pequeñas, así que no se podría notar una diferencia en tiempo o memoria respecto a cada algoritmo. Sin embargo, para soluciones más grandes, BFS toma el liderazgo porque va priorizando varios frentes de búsqueda en vez de ir sin un patrón específico, lo que puede acelerar el descubrimiento de la salida.

### 3. ¿Cómo afecta el tamaño del laberinto a la eficiencia de BFS y DFS en términos de tiempo y espacio?

#### BFS (Breadth-First Search)

- Tiempo: En el peor caso, explora todos los nodos, con complejidad O(V + E). Si el laberinto es grande, el tiempo de ejecución aumenta considerablemente.
- Espacio: Almacena todos los nodos a nivel de profundidad actual, lo que puede requerir O(mn) memoria en un laberinto de tamaño m × n. En laberintos grandes, esto lo vuelve ineficiente.

#### DFS (Depth-First Search)

- Tiempo: También tiene complejidad O(V + E), pero puede perder tiempo explorando caminos largos sin encontrar la mejor solución.
- Espacio: Solo almacena los nodos en la pila de recursión, usando O(D) memoria, donde D es la profundidad del laberinto. Es más eficiente en memoria que BFS en laberintos grandes.

#### Conclusión:
Si el laberinto es grande, BFS se vuelve ineficiente por su alto consumo de memoria, mientras que DFS es más viable en términos de espacio. Sin embargo, BFS sigue siendo mejor si se necesita el camino más corto.