import copy
import numpy as np
from math import sqrt


def find_max_element(matrix):
    max_el = 0.
    max_indx = (0, 0)
    for index, el in np.ndenumerate(matrix):
        if ((index[0] != index[1])):
            if (max_el < abs(el)):
                max_el = abs(el)
                max_indx = index
    return max_el, max_indx

def create_matrix_T(matrix, index): # index is tuple (i, j)
    matrix_T = np.zeros_like(matrix, dtype=float)
    np.fill_diagonal(matrix_T, 1)
    p = 2 * matrix[index]
    q = matrix[index[1]][index[1]] - matrix[index[0]][index[0]]
    if (q == 0):
        c = sqrt(2) / 2
        s = sqrt(2) / 2
    else:
        d = sqrt(p ** 2 + q ** 2)
        r = abs(q) / (2 * d)
        c = sqrt(0.5 + r)
        if (p * q >= 0):
            s = sqrt(0.5 - r)
        else:
            s = -sqrt(0.5 - r)
    matrix_T[index[0]][index[0]] = c
    matrix_T[index[1]][index[1]] = c
    matrix_T[index[0]][index[1]] = s
    matrix_T[index[1]][index[0]] = -s

    return matrix_T

def create_matrix_B(matrix, matrix_T, index):
    i = index[0]
    j = index[1]
    matrix_B = matrix.copy()
    # new diagonal elements
    matrix_B[i][i] = (matrix_T[i][i] ** 2) * matrix[i][i] + (matrix_T[i][j] ** 2) * matrix[j][j] - 2 * matrix_T[i][i] * matrix_T[i][j] * matrix[i][j]
    matrix_B[j][j] = (matrix_T[i][j] ** 2) * matrix[i][i] + (matrix_T[i][i] ** 2) * matrix[j][j] + 2 * matrix_T[i][i] * matrix_T[i][j] * matrix[i][j]
    # other elements of B
    matrix_B[i][j] = 0.
    matrix_B[j][i] = 0.

    for m in range(matrix.shape[0]):
        if ((m != i) & (m != j)):
            matrix_B[i][m] = matrix_T[i][i] * matrix[m][i] - matrix_T[i][j] * matrix[m][j]
            matrix_B[m][i] = matrix_T[i][i] * matrix[m][i] - matrix_T[i][j] * matrix[m][j]
            matrix_B[j][m] = matrix_T[i][j] * matrix[m][i] + matrix_T[i][i] * matrix[m][j]
            matrix_B[m][j] = matrix_T[i][j] * matrix[m][i] + matrix_T[i][i] * matrix[m][j]
    return matrix_B

def check_stop_condition(matrix_B, eps):
    for index, el in np.ndenumerate(matrix_B):
        if (index[0] != index[1]):
            if (abs(el) > eps):
                return False
    return True

def get_trace_matrix(matrix):
    trace = 0
    for index, el in np.ndenumerate(matrix):
        if (index[0] == index[1]):
            trace += el
    return trace