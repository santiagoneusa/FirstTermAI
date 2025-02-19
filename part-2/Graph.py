from collections import deque
from Node import Node

class Graph:
    def __init__(self, start_state, final_state, graph):
        self.start_state = start_state
        self.final_state = final_state
        self.graph = graph

    def bfs(self):
        start_node = Node(self.start_state, None, self.graph)
        frontier = deque([start_node])
        reached = {start_node.state: start_node}

        while frontier:
            node = frontier.popleft()

            for neighbor_state in node.get_neighbors():
                if neighbor_state in reached:
                    neighbor_node = reached[neighbor_state]
                else:
                    neighbor_node = Node(neighbor_state, node, self.graph)
                    reached[neighbor_state] = neighbor_node

                if neighbor_state == self.final_state:
                    return neighbor_node
                else:
                    frontier.append(neighbor_node)

        return None

    def dfs(self):
        pass