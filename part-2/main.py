import heapq

edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'),
    ('D', 'G'),
    ('E', 'H'), ('E', 'I'),
    ('F', 'J'),
    ('I', 'J')
]


def bfs(start, end, edges):
    start = 'A'
    frontier = search_edges('start')

    while frontier:
