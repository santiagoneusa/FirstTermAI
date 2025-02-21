# Ejecución del Código

Una vez descargado el repositorio, ingrese a la carpeta denominada `part-2`:

```bash
cd part-2
```

Allí dentro, ejecute el programa `main.py`:

```bash
python main.py
```

Ese programa responde los numerales 1, 2 y 3 del informe 2.

# IDS vs. BFS

## Memoria

La búsqueda en profundidad iterativa (IDS) usa menos memoria que la búsqueda por amplitud (BFS). En cualquier punto del DFS (que es lo que internamente hace el IDS), usa una cantidad de memoria proporcional a los vecinos de un solo camino a través del grafo; mientras que el BFS usa una cantidad de memoria proporcional a la amplitud del grafo.

Esto significa que BFS, al explorar por niveles, debe almacenar todos los nodos de un nivel antes de pasar al siguiente. En el peor caso, si el factor de ramificación es *b* y la profundidad de la solución es *d*, BFS puede llegar a almacenar hasta *O(b^d)* nodos en memoria, lo que lo hace inviable en grafos grandes.

En contraste, IDS utiliza DFS con profundidades crecientes y solo mantiene en memoria la pila de recursión de la búsqueda actual, lo que reduce su consumo de memoria a *O(d)* en el peor caso. Aunque IDS reexplora nodos en distintas iteraciones, su uso de memoria sigue siendo mucho menor que BFS, lo que lo convierte en una opción viable cuando la memoria es un recurso crítico.

## Tiempo

### BFS

- Explora los nodos en niveles y solo los visita una vez, gracias al conjunto `reached`.
- La complejidad temporal en el peor caso es *O(b^d)*, donde *b* es el factor de ramificación y *d* es la profundidad de la solución.
- Es más eficiente en términos de tiempo porque no reexplora nodos.

### IDS

- Llama a DLS repetidamente con profundidades crecientes.
- Como cada ejecución de DLS descarta la información de la búsqueda anterior, los nodos cercanos a la raíz se expanden muchas veces.
- En el peor caso, IDS puede tomar hasta *O(b^d)\*d* tiempo, ya que expande los primeros niveles múltiples veces.

IDS usa menos memoria que BFS, pero es más ineficiente temporalmente porque repite exploraciones. Sin embargo, esta pérdida suele ser aceptable si el factor de ramificación *b* no es demasiado grande y la solución está a poca profundidad.