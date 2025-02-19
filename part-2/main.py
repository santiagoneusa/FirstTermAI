if __name__ == '__main__':

    from Graph import Graph

    def main():
        layout = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B', 'G'], 
            'E': ['B', 'H', 'I'],
            'F': ['C', 'J'],
            'G': ['D'],
            'H': ['E'],
            'I': ['E', 'J'],
            'J': ['F', 'I']
        }
        initial_state = 'A'
        final_state = 'J'

        graph = Graph(initial_state, final_state, layout)

        node_solution = graph.bfs()
        node_solution.reconstruct_path()

        # node_solution = graph.dfs()
        # node_solution.reconstruct_path()

    main()
