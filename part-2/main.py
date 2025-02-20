if __name__ == '__main__':

    from Graph import Graph
    import time
    import tracemalloc

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

        # BFS Benchmark
        print('Running BFS...')
        tracemalloc.start()
        start_time = time.time()

        node_solution = graph.bfs()

        end_time = time.time()
        mem_bfs = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        node_solution.reconstruct_path()
        print(f'BFS Time: {end_time - start_time:.6f} seconds')
        print(f'BFS Memory Usage: {mem_bfs[1] / 1024:.2f} KB (Peak)')

        # IDS Benchmark
        print('\nRunning IDS...')
        tracemalloc.start()
        start_time = time.time()

        node_solution = graph.ids(max_depth)

        end_time = time.time()
        mem_ids = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if node_solution is None:
            print('Solution not found, try a new maximum depth.')
        else:
            node_solution.reconstruct_path()
        
        print(f'IDS Time: {end_time - start_time:.6f} seconds')
        print(f'IDS Memory Usage: {mem_ids[1] / 1024:.2f} KB (Peak)')

    main()
