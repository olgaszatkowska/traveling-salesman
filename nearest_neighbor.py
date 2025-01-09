from common import distance


def nearest_neighbor(points: list[list[int]]):
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

    return tour
