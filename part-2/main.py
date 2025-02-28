if __name__ == '__main__':

    from Maze import Maze
    # from RosManager import RosManager

    def main():
        actions = {
            (0, -1): 'Left',
            (0, 1): 'Right',
            (-1, 0): 'Up',
            (1, 0): 'Down',
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
        print(path)

        # ros_manager = RosManager(path)
        # ros_manager.execute_path()
        # ros_manager.exit()


    main()
