class Node:
    def __init__(self, action_taken, coordinates, path_cost, parent):
        self.action_taken = action_taken
        self.coordinates = coordinates
        self.path_cost = path_cost
        self.parent = parent
        self.neighbors = []

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def set_neighbors(self, actions, maze):
        coordinate_x = self.coordinates[0]
        coordinate_y = self.coordinates[1]

        for movement, action_taken in [x for x in actions.items()]:
            movement_x = movement[0]
            movement_y = movement[1]

            neighbor_coordinates = (coordinate_x + movement_x, coordinate_y + movement_y)

            if 0 <= neighbor_coordinates[0] < len(maze) and 0 <= neighbor_coordinates[1] < len(maze[0]):
                if maze[neighbor_coordinates[0]][neighbor_coordinates[1]] in [' ', 'S', 'E']:
                    self.neighbors.append((neighbor_coordinates, action_taken))

    def reconstruct_path(self):
        path_coordinates, path_actions_taken = [], []
        node = self

        while node:
            path_coordinates.insert(0, node.coordinates)
            path_actions_taken.insert(0, node.action_taken)
            node = node.parent

        print('Exit:', path_coordinates[-1])
        print('Path to exit:', path_coordinates)
        print('Path actions to exit:', path_actions_taken)
        print()
