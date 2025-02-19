if __name__ == '__main__':

    from Maze import Maze

    def main():
        actions = {
            (0, 1): 'Right',
            (1, 0): 'Down',
            (0, -1): 'Left',
            (-1, 0): 'Up',
        }

        matrix_multiple_exits = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'S', ' ', ' ', '#', ' ', ' ', 'E', '#', '#'],
            ['#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
            ['#', '#', '#', '#', '#', ' ', '#', 'E', '#', '#'],
            ['#', ' ', 'E', ' ', '#', ' ', ' ', ' ', '#', '#'],
            ['#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#'],
            ['#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]

        method = 'euclidean'
        maze = Maze(actions, matrix_multiple_exits, method)

        print('Multiple exits')
        maze.find_start_and_exits()
        maze.solve()

        print('Nearest exit among multiple exits')
        maze.find_start_and_exits(nearest=True)
        maze.solve()

    main()
