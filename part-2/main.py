if __name__ == '__main__':

    from Maze import Maze
    # from RosManager import RosManager

    def main():
        actions = {
            (0, -1): 'west',
            (0, 1): 'east',
            (-1, 0): 'north',
            (1, 0): 'south',
        } 

        matrix = maze = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', 'E'],
            ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
            ['#', 'S', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' '],
            ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' '],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ']
        ]

        maze = Maze(actions, matrix)
        maze.find_start_and_exits()

        node_solution = maze.solve()
        path = node_solution.reconstruct_path()

        # Inicialmente, asumimos que el robot está mirando hacia el sur
        looking_at = 'south'

        formated_path = []
        for direction in path:
            if direction == 'north':
                if looking_at == 'north':
                    formated_path.append('forward')
                elif looking_at == 'south':
                    formated_path.extend(['turn right', 'turn right', 'forward'])
                elif looking_at == 'west':
                    formated_path.extend(['turn right', 'forward'])
                elif looking_at == 'east':
                    formated_path.extend(['turn left', 'forward'])
                looking_at = 'north'

            elif direction == 'south':
                if looking_at == 'north':
                    formated_path.extend(['turn right', 'turn right', 'forward'])
                elif looking_at == 'south':
                    formated_path.append('forward')
                elif looking_at == 'west':
                    formated_path.extend(['turn left', 'forward'])
                elif looking_at == 'east':
                    formated_path.extend(['turn right', 'forward'])
                looking_at = 'south'

            elif direction == 'west':
                if looking_at == 'north':
                    formated_path.extend(['turn left', 'forward'])
                elif looking_at == 'south':
                    formated_path.extend(['turn right', 'forward'])
                elif looking_at == 'west':
                    formated_path.append('forward')
                elif looking_at == 'east':
                    formated_path.extend(['turn right', 'turn right', 'forward'])
                looking_at = 'west'

            elif direction == 'east':
                if looking_at == 'north':
                    formated_path.extend(['turn right', 'forward'])
                elif looking_at == 'south':
                    formated_path.extend(['turn left', 'forward'])
                elif looking_at == 'west':
                    formated_path.extend(['turn right', 'turn right', 'forward'])
                elif looking_at == 'east':
                    formated_path.append('forward')
                looking_at = 'east'

        print(formated_path)
        # ros_manager = RosManager(path)
        # ros_manager.execute_path()
        # ros_manager.exit()


    main()
