import random
import math

from common import generate_tour, plot, visualize_tour, tour_length


def accept_solution(delta, temperature):
    if delta < 0:
        return True, 1

    r = random.random()

    acceptance_th = math.exp(-delta / temperature)

    if r < acceptance_th:
        return True, acceptance_th

    return False, acceptance_th


def generate_new_solution_permutation(tour):
    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour


def simulated_annealing(t_max, t_min, e_th, a, tour):
    # T_max = the maximum temperature
    # T_min = the minimum temperature for stopping the algorithm
    # E_th = the energy threshold to stop the algorithm
    # alpha = the cooling factor

    temperature = t_max
    energy = tour_length(tour)

    ths = []

    while temperature > t_min and energy > e_th:
        candidate_tour = generate_new_solution_permutation(tour)
        candidate_energy = tour_length(candidate_tour)
        energy_delta = candidate_energy - energy

        accept, th = accept_solution(energy_delta, temperature)
        ths.append(th)

        if accept:
            tour = candidate_tour
            energy = candidate_energy

        temperature = temperature / a

    plot(ths, label1="acceptance th", title="Acceptance th over time")
    return tour


if __name__ == "__main__":
    initial_tour = generate_tour(num_points=50, x_range=(0, 1000), y_range=(0, 1000))
    initial_tour_lenght = tour_length(initial_tour)

    new_tour = simulated_annealing(
        t_max=100000, t_min=0.1, e_th=1e-10, a=1 + 1e-4, tour=initial_tour
    )
    new_tour_length = tour_length(new_tour)
    print(initial_tour_lenght, new_tour_length)
    visualize_tour(initial_tour, "initial tour")
    visualize_tour(new_tour, "new tour")
