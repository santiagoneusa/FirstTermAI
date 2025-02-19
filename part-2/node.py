class Node:
    def __init__(self, state: str, parent: 'Node', graph: dict):
        self.state: str = state
        self.parent: 'Node' = parent
        self.neighbors: dict = graph[state]

    def get_neighbors(self):
        return self.neighbors

    def reconstruct_path(self):
        node = self
        path = [self.state]

        while node.parent != None:
            path.insert(0, node.parent.state)
            node = node.parent
        
        print(f'Nodo inicial: {path[0]}')
        print(f'Nodo final: {path[-1]}')
        print(f'Path: {path}\n')
