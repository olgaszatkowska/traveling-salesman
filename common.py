from math import sqrt, inf
import random

import matplotlib.pyplot as plt
import networkx as nx


def distance(point_1, point_2):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)


def generate_tour(num_points, x_range, y_range):
    points = [
        (random.randint(*x_range), random.randint(*y_range)) for _ in range(num_points)
    ]
    return [points[i] for i in range(len(points) - 1)] + [points[-1], points[0]]

def tour_length(tour):
    total = 0
    for i, vertex in enumerate(tour):
        next_i = i + 1 if i + 1 < len(tour) else 0
        total += distance(vertex, tour[next_i])

    return total


def visualize_tour(points, figname):
    G = nx.Graph()
    edges = [(points[i], points[i + 1]) for i in range(len(points) - 1)]
    G.add_edges_from(edges)
    pos = {point: point for point in points}
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_weight="bold",
    )
    plt.savefig(f"tours_visualized/{figname}")
    plt.close()


def plot(
    values1,
    label1="Series 1",
    x_label="Index",
    title="Series",
):
    indexes = list(range(1, len(values1) + 1))

    plt.figure(figsize=(16, 10))
    plt.plot(indexes, values1, marker="o", linestyle="", label=label1, color="b")

    plt.xlabel(x_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{title}")
    plt.close()
