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

        for movement, action_taken in actions.items():
            movement_x = movement[0]
            movement_y = movement[1]

            wall_coordinates = (coordinate_x + movement_x, coordinate_y + movement_y)
            neighbor_coordinates = (coordinate_x + (movement_x * 2), coordinate_y + (movement_y * 2))

            if 0 <= neighbor_coordinates[0] < len(maze) and 0 <= neighbor_coordinates[1] < len(maze[0]):
                if maze[wall_coordinates[0]][wall_coordinates[1]] in [' ', 'S', 'E']:
                    self.neighbors.append((neighbor_coordinates, action_taken))

    def get_neighbors(self):
        return self.neighbors

    def reconstruct_path(self, initial_looking_at='south'):
        path_actions_taken = []
        node = self

        while node.parent is not None:
            path_actions_taken.insert(0, node.action_taken)
            node = node.parent

        # Formatear el camino
        looking_at = initial_looking_at
        formated_path = []
        for direction in path_actions_taken:
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

        return formated_path
