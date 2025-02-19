import heapq
from DistanceManager import DistanceManager
from Node import Node


class Maze:

    def __init__(self, actions, matrix, method):
        self.actions = actions
        self.matrix = matrix
        self.method = method
        self.start_coordinates = ()
        self.exit_coordinates = []

    def get_distance(self, coordinates1, coordinates2):
        return DistanceManager.get_distance(self.method, coordinates1, coordinates2)

    def find_start_and_exits(self, nearest=False):
        possible_exits = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 'S':
                    self.start_coordinates = (i, j)
                elif self.matrix[i][j] == 'E':
                    possible_exits.append((i, j))

        if nearest:
            self.exit_coordinates = [
                min(
                    possible_exits,
                    key=lambda exit_coordinate: self.get_distance(self.start_coordinates, exit_coordinate)
                )
            ]
        else:
            self.exit_coordinates = possible_exits

    def solve(self):
        for exit_coordinate in self.exit_coordinates:
            node_solution = self.solve_with_exit(exit_coordinate)
            node_solution.reconstruct_path()

    def solve_with_exit(self, exit_coordinate):
        start_node = Node(None, self.start_coordinates, 0, None)
        start_node.set_neighbors(self.actions, self.matrix)
        frontier = [
            (
                self.get_distance(start_node.coordinates, exit_coordinate),
                start_node
            )
        ]
        heapq.heapify(frontier)

        reached_nodes = {start_node.coordinates: start_node}

        while frontier:
            _, node = heapq.heappop(frontier)

            if node.coordinates == exit_coordinate:
                return node

            for neighbor_coordinates, action_taken in node.neighbors:
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
                            self.get_distance(neighbor_coordinates, exit_coordinate),
                            reached_nodes[neighbor_coordinates]
                        )
                    )

        return None
