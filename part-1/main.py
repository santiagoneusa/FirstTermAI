from Maze import Maze

def main():
    actions = {
        (0, 1): 'Right',
        (1, 0): 'Down',
        (0, -1): 'Left',
        (-1, 0): 'Up',
    }

    matrix = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', '#', ' ', '#', ' ', 'E', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#']
    ]

    method = 'manhatan'
    maze = Maze(actions, matrix, method)
    maze.find_start_and_exits()
    maze.solve()

if __name__ == '__main__':
    main()
