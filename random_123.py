import random
from copy import deepcopy

from common import connect_beginning_to_end


def algorithm_123(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    points = deepcopy(points)
    random.shuffle(points)
    
    return connect_beginning_to_end(points)
