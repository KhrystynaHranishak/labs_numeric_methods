import numpy as np
import copy

def get_norm_vector(vector): # count cubic norm
    vector = np.array(vector)
    norm = abs(vector[0])
    for i in range(1, len(vector)):
        if (norm < abs(vector[i])):
            norm = abs(vector[i])
    return norm

def get_norm_matrix(matrix): # count cubic norm
    matrix = np.array(matrix)
    norm = 0.
    for i in range(matrix.shape[0]):
        sum_row = 0.
        for j in range(matrix.shape[1]):
            sum_row += abs(matrix[i][j])
        if (norm < sum_row):
            norm = sum_row
    return norm

def change_A2B(matrix, vector_b):
    matrix = np.array(matrix)
    vector_b = np.array(vector_b)
    B = copy.deepcopy(matrix)
    b = copy.deepcopy(vector_b)
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            B[i][j] = float(B[i][j]) / float(matrix[i][i])
        b[i] = b[i] / float(matrix[i][i])
    E = np.zeros_like(B, dtype=float)
    np.fill_diagonal(E, val=1)
    B = E - B
    return B, b

def modificate_B_GZ(matrix, vector_b):
    B = copy.deepcopy(matrix)
    b = copy.copy(vector_b)
    if (get_norm_matrix(matrix) > 1):
        for i in range(B.shape[0]):
            sum_row = 0.
            for j in range(B.shape[1]):
                sum_row += abs(B[i][j])
            for k in range(B.shape[1]):
                B[i][k] = B[i][k] / sum_row
            b[i] = b[i] / sum_row
    B_new = copy.deepcopy(B)
    for i in range(B_new.shape[0]):
        for j in range(B_new.shape[1]):
            B_new[i][j] = float(B_new[i][j]) / float(B[i][i])
        b[i] = b[i] / float(B[i][i])
    E = np.zeros_like(B_new, dtype=float)
    np.fill_diagonal(E, val=1)
    print(B_new)
    B_new = E - B_new

    return B_new, b