import numpy as np
import copy
from help_functions import get_norm_vector, get_norm_matrix, change_A2B, modificate_B_GZ

def Gauss_Zeidel(matrix, vector_b, eps, max_iterations):
    error = False
    B, b = change_A2B(matrix, vector_b)
    B_L = np.zeros_like(B, dtype = float)
    B_R = np.zeros_like(B, dtype=float)
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if (j < i):
                B_L[i][j] = B[i][j]
            if (j > i):
                B_R[i][j] = B[i][j]
    q_R = get_norm_matrix(B_R)
    q_L = get_norm_matrix(B_L)
    counter_iterations = 0
    x_start = np.zeros(len(b), dtype=np.float64) + 100
    x_next = B.dot(x_start) + b
    solutions_list = [x_start, x_next]
    if ((q_R / (1 - q_L) >= 1) | (q_L >= 1)):
        error = True
    else:
        while(get_norm_vector(x_next - x_start) > eps * q_R / (1 - q_L)):
            x_start = copy.copy(x_next)
            x_next = np.zeros(len(b), dtype=np.float64)
            for i in range(B.shape[0]):
                for j in range(B.shape[1]):
                    if (j < i):
                        x_next[i] += B[i][j] * x_next[j]
                    elif (j > i):
                        x_next[i] += B[i][j] * x_start[j]
                x_next[i] += b[i]
            counter_iterations += 1
            solutions_list.append(x_next)
            if (counter_iterations >= max_iterations):
                error = True
                break
    return x_next, error, counter_iterations, solutions_list