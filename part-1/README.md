# Ejecución del Código

Una vez descargado el repositorio, ingrese a la carpeta denominada `part-1`:

```bash
cd part-1
```

Allí dentro, ejecute el programa `main.py`:

```bash
python main.py
```

Ese programa contiene el problema planteado de la misma forma que está en el jupyter, es decir, no tiene los cambios que responden a las preguntas 1, 2 y 3.

---

# Preguntas

## 1. ¿Cómo cambia el comportamiento del algoritmo si cambiamos la función de costo?

El propósito de la función de costo es definir cómo se mide la distancia entre los nodos en la búsqueda del camino más corto. En este caso, la distancia actúa como una heurística que guía la exploración del laberinto.

El problema funciona con distancia Manhattan, pero creamos una interfaz desde la que se pudiera interactuar con múltiples distancias en un archivo `DistanceManager`. Para escoger otro método de cálculo de la distancia, pero que siga con la misma lógica, desarrollamos el método euclidiano.

### Comparación entre Manhattan y Euclidiana
- **Manhattan:** Se usa en movimientos restringidos a una cuadrícula, permitiendo solo desplazamientos en las direcciones arriba, abajo, izquierda y derecha. Esto puede resultar en caminos con más giros.

- **Euclidiana:** Considera la distancia en línea recta entre dos puntos. Si se permiten movimientos diagonales, esta métrica puede producir caminos más cortos y eficientes.

### Impacto en el algoritmo
- Si el laberinto permite solo movimientos ortogonales, la distancia Manhattan es más adecuada.

- Si se permite el movimiento diagonal, la distancia Euclidiana puede generar rutas más eficientes.

- La heurística afecta la exploración del laberinto, pudiendo alterar el orden en que se visitan los nodos y, en algunos casos, reduciendo la cantidad de nodos explorados.

Para probar ambas distancias, ejecute:

```bash
python main1.py
```

---

## 2. ¿Qué pasa si hay múltiples salidas en el laberinto? ¿Cómo podrías modificar el algoritmo para manejar esto?

Para resolver este problema hay dos aproximaciones: tomar la salida más cercana a la entrada o hallar el camino para todas las salidas posibles.

### Hallar el camino para todas las salidas posibles

En la implementación dada por el profesor ya había una función encargada de hallar la entrada y salida del laberinto. Lo que hicimos fue cambiar una línea de código para que adjuntara en una lista todas las casillas que tenían como símbolo `E`.

**Archivo `Maze.py`:**

```python
possible_exits = []

for i in range(len(self.matrix)):
    for j in range(len(self.matrix[0])):
        if self.matrix[i][j] == 'S':
            self.start_coordinates = (i, j)
        elif self.matrix[i][j] == 'E':
            possible_exits.append((i, j))
```

Así mismo, se creó una función `solve`, que itera sobre la lista de salidas posibles e imprime los caminos asociados a cada nodo solución.

**Archivo `Maze.py`:**

```python
def solve(self):
    for exit_coordinate in self.exit_coordinates:
        node_solution = self.solve_with_exit(exit_coordinate)
        node_solution.reconstruct_path()
```

### Salida más cercana a la entrada

Aunque el algoritmo soluciona la multiplicidad de salidas mediante un proceso iterativo, se usó la función heurística para evaluar también cuál es la mejor solución.

La función `find_start_and_exits()` recibe un parámetro `nearest`, que por defecto es `False`, pero si se cambia a `True` permite hallar la salida con la distancia mínima a la entrada.

**Archivo `Maze.py`, función `find_start_and_exits`:**

```python
if nearest:
    self.exit_coordinates = [
        min(
            possible_exits,
            key=lambda exit_coordinate: self.get_distance(self.start_coordinates, exit_coordinate)
        )
    ]
```

De esta forma se crea una lista iterable con un solo valor, que se usa en la función `solve` anteriormente vista.

Este método reduce el tiempo de ejecución en laberintos grandes con muchas salidas, ya que solo se explora un camino en lugar de calcular todos.

### Nota

Para ver un ejemplo con múltiples soluciones, ejecute el programa `main2.py`:

```bash
python main2.py
```

---

## 3. Modifica el laberinto por uno más grande y con otros tipos de obstáculos además de pared.

### ¿Qué limitación encuentras en el algoritmo?

Para hacer la exploración del laberinto, usamos una función que descubre los vecinos de las celdas exploradas. El código original era:

```python
if maze[neighbor_coordinates[0]][neighbor_coordinates[1]] != '#':
    self.neighbors.append((neighbor_coordinates, action_taken))
```

Aquí, el símbolo `#` representa un obstáculo, pero notamos que solo hay un tipo de obstáculo posible. Para generalizar los obstáculos, decidimos invertir la lógica y considerar obstáculo todo lo que no sea espacio, entrada o salida.

**Archivo `Node.py`, función `set_neighbors`:**

```python
if maze[neighbor_coordinates[0]][neighbor_coordinates[1]] not in [' ', 'S', 'E']:
    self.neighbors.append((neighbor_coordinates, action_taken))
```

Con esta nueva lógica, respaldamos tanto los `#` como cualquier otro símbolo futuro que represente un obstáculo.

### Impacto de la mejora
- Permite agregar nuevos tipos de obstáculos sin modificar el código.

- Hace que el algoritmo sea más genérico y fácil de extender.

- Reduce la posibilidad de errores en la interpretación del mapa.

### Nota

Para ver un ejemplo con múltiples obstáculos, ejecute el archivo `main3.py`:

```bash
python main3.py
```
