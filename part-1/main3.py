from Maze import Maze

def main():
    actions = {
        (0, 1): 'Right',
        (1, 0): 'Down',
        (0, -1): 'Left',
        (-1, 0): 'Up',
    }

    matrix_multiple_obstacles = [
        ['#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', 'X', ' ', '#', 'O', ' ', 'X', '#', '#'],
        ['#', '#', '#', ' ', '#', '*', '#', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
        ['#', '#', '#', '#', 'X', ' ', '#', 'E', '#', '#'],
        ['#', ' ', 'X', ' ', '#', ' ', '*', ' ', '#', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
        ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '*', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    method = 'euclidean'

    maze = Maze(actions, matrix_multiple_obstacles, method)
    maze.find_start_and_exits()

    print('Multiple obstacles\n')
    maze.solve()

if __name__ == '__main__':
    main()
