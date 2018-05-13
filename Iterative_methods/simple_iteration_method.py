import numpy as np
import copy
from help_functions import get_norm_vector, get_norm_matrix, change_A2B

def simple_iteration(matrix, vector_b, eps, max_iteration):
    error = False
    B, b = change_A2B(matrix, vector_b)
    q = get_norm_matrix(B)
    x_start = np.zeros(len(b), dtype=np.float64)
    x_next = B.dot(x_start) + b
    solutions_list = [x_start, x_next]
    counter_iterations = 0
    if (q >= 1):
        error = True
    else:
        while (get_norm_vector(x_next - x_start) > (1 / q - 1) * eps):
            x_start = copy.copy(x_next)
            x_next = B.dot(x_start) + b
            solutions_list.append(x_next)
            counter_iterations += 1
            if (counter_iterations >= max_iteration):
                error = True
                break
    return x_next, error, counter_iterations, solutions_list
