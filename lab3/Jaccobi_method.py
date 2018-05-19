import numpy as np
import help_functions as hf

def Jaccobi_method(matrix, eps):
    list_Ti = []
    sequence_max = []
    k = 0
    while True:
        #print(matrix)
        max_el, index = hf.find_max_element(matrix)
        #print(max_el, index)
        sequence_max.append(max_el)
        matrix_T = hf.create_matrix_T(matrix, index)
        #print(matrix_T)
        matrix_B = hf.create_matrix_B(matrix, matrix_T, index)
        #print(matrix_B)
        if not (hf.check_stop_condition(matrix_B, eps)):
            matrix = matrix_B.copy()
            list_Ti.append(matrix_T)
        else:
            list_Ti.append(matrix_T)
            break
    return matrix_B, list_Ti

def find_vectors(list_Ti):
    product = np.zeros_like(list_Ti[0], dtype=float)
    np.fill_diagonal(product, 1)
    for matrix in list_Ti:
        product = product.dot(matrix)
    return product
