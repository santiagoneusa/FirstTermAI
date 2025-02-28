import heapq
from Node import Node


class Maze:

    def __init__(self, actions, matrix):
        self.actions = actions
        self.matrix = matrix
        self.start_coordinates = ()
        self.exit_coordinates = ()

    def get_distance(coordinates1, coordinates2):
        return abs(coordinates1[0] - coordinates2[0]) + abs(coordinates1[1] - coordinates2[1])

    def find_start_and_exits(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 'S':
                    self.start_coordinates = (i, j)
                elif self.matrix[i][j] == 'E':
                    self.exit_coordinates = (i, j)

    def solve(self):
        start_node = Node(None, self.start_coordinates, 0, None)
        start_node.set_neighbors(self.actions, self.matrix)
        frontier = [
            (
                Maze.get_distance(start_node.coordinates, self.exit_coordinates),
                start_node
            )
        ]
        heapq.heapify(frontier)

        reached_nodes = {start_node.coordinates: start_node}

        while frontier:
            _, node = heapq.heappop(frontier)

            if node.coordinates == self.exit_coordinates:
                return node

            for neighbor_coordinates, action_taken in node.get_neighbors():
                new_path_cost = node.path_cost + 1

                if neighbor_coordinates not in reached_nodes or new_path_cost < reached_nodes[neighbor_coordinates].path_cost:
                    if neighbor_coordinates in reached_nodes:
                        reached_nodes[neighbor_coordinates].path_cost = new_path_cost
                        reached_nodes[neighbor_coordinates].parent = node
                        reached_nodes[neighbor_coordinates].action_taken = action_taken
                    else:
                        reached_nodes[neighbor_coordinates] = Node(
                            action_taken, neighbor_coordinates, new_path_cost, node
                        )

                    reached_nodes[neighbor_coordinates].set_neighbors(
                        self.actions, self.matrix
                    )

                    heapq.heappush(
                        frontier,
                        (
                            Maze.get_distance(neighbor_coordinates, self.exit_coordinates),
                            reached_nodes[neighbor_coordinates]
                        )
                    )

        return None
