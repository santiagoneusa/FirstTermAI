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
        max_depth = 3

        graph = Graph(initial_state, final_state, layout)

        print('Running BFS...')
        node_solution = graph.bfs()
        node_solution.reconstruct_path()

        print('Running IDS...')
        node_solution = graph.ids(max_depth)
        if node_solution == None:
            print('Solution not found, try a new maximum depth.')
            return -1

        node_solution.reconstruct_path()

    main()
