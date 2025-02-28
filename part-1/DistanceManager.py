import math

class DistanceManager:
    def get_distance(method, coordinates1, coordinates2):
        return getattr(DistanceManager, method)(coordinates1, coordinates2)

    def manhatan(coordinates1, coordinates2):
        return abs(coordinates1[0] - coordinates2[0]) + abs(coordinates1[1] - coordinates2[1])

    def euclidean(coordinates1, coordinates2):
        return math.sqrt((coordinates1[0] - coordinates2[0]) ** 2 + (coordinates1[1] - coordinates2[1]) ** 2)
