from copy import deepcopy
from common import distance, connect_beginning_to_end


def nearest_neighbor(points: list[list[int]]):
    points = deepcopy(points)
    tour = [points[0]]
    points.remove(points[0])

    while points:
        current_point = tour[-1]
        shortest_distance = float("inf")

        for point in points:
            candidate_distance = distance(current_point, point)

            if shortest_distance > candidate_distance:
                shortest_distance = candidate_distance
                new_neighbor = point

        tour.append(new_neighbor)
        points.remove(new_neighbor)

    return connect_beginning_to_end(tour)
