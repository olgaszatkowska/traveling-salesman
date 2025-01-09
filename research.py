import time
import matplotlib.pyplot as plt

from common import generate_tour, tour_length

from farthest_apart import farthest_insertion
from  nearest_neighbor import nearest_neighbor


num_points_range = range(10, 500, 10)
ff_tour_lengths = []
ff_elapsed_times = []
nn_tour_lengths = []
nn_elapsed_times = []

for i in num_points_range:
    tour = generate_tour(num_points=i, x_range=(0, 1000), y_range=(0, 1000))

    start_time = time.perf_counter()
    ff_tour = farthest_insertion(tour)
    end_time = time.perf_counter()
    ff_elapsed_time = end_time - start_time

    ff_tour_lengths.append(tour_length(ff_tour))
    ff_elapsed_times.append(ff_elapsed_time)

    start_time = time.perf_counter()
    nn_tour = nearest_neighbor(tour)
    end_time = time.perf_counter()
    nn_elapsed_time = end_time - start_time

    nn_tour_lengths.append(tour_length(nn_tour))
    nn_elapsed_times.append(nn_elapsed_time)

plt.figure(figsize=(10, 5))
plt.plot(num_points_range, ff_tour_lengths, label='Farthest Insertion', color='red')
plt.plot(num_points_range, nn_tour_lengths, label='Nearest Neighbor', color='blue')
plt.xlabel('Number of Points')
plt.ylabel('Tour Length')
plt.title('Tour Length vs Number of Points')
plt.legend()
plt.grid(True)
plt.savefig("plots/tour_lengths")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(num_points_range, ff_elapsed_times, label='Farthest Insertion', color='red')
plt.plot(num_points_range, nn_elapsed_times, label='Nearest Neighbor', color='blue')
plt.xlabel('Number of Points')
plt.ylabel('Elapsed Time (s)')
plt.title('Elapsed Time vs Number of Points')
plt.legend()
plt.grid(True)
plt.savefig("plots/time_complexity")
plt.close()
