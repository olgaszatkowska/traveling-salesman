from common import distance, connect_beginning_to_end


def _find_furthest_apart_cities(distances, n):
    max_dist = 0
    p1, p2 = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] > max_dist:
                max_dist = distances[i][j]
                p1, p2 = i, j

    return p1, p2


def _find_farthest_point_from_tour(n, visited, distances, tour):
    farthest_point = -1
    max_distance = -1
    for i in range(n):
        if not visited[i]:
            min_dist_to_tour = min(distances[i][j] for j in tour)
            if min_dist_to_tour > max_distance:
                max_distance = min_dist_to_tour
                farthest_point = i

    return farthest_point


def farthest_insertion(points):
    n = len(points)

    distances = [[distance(points[i], points[j]) for j in range(n)] for i in range(n)]
    visited = [False] * n

    p1, p2 = _find_furthest_apart_cities(distances, n)

    tour = [p1, p2]
    visited[p1] = True
    visited[p2] = True

    while len(tour) < n:
        farthest_point = _find_farthest_point_from_tour(n, visited, distances, tour)
        best_position = -1
        min_increase = float("inf")
        for i in range(len(tour)):
            j = (i + 1) % len(tour)
            candidate_increase = (
                distances[tour[i]][farthest_point]
                + distances[farthest_point][tour[j]]
                - distances[tour[i]][tour[j]]
            )
            if candidate_increase < min_increase:
                min_increase = candidate_increase
                best_position = j

        tour.insert(best_position, farthest_point)
        visited[farthest_point] = True

    tour_as_points = [points[i] for i in tour]
    return connect_beginning_to_end(tour_as_points)
