import numpy as np
import simple_iteration_method as sim
from help_functions import change_A2B
import Gauss_Zeidel_method as GZ

def print_out(matrix, vector_b, eps, max_iteration):
    matrix = np.array(matrix)
    vector_b = np.array(vector_b)

    B, c = change_A2B(matrix, vector_b)

    print('The initial matrix is \n {}'.format(matrix))
    print('The initial vector is {}'.format(vector_b))
    print('\n')

    print('The changed matrix is \n {}'.format(B))
    print('The changed vector b is {}'.format(c))
    print('\n')

    print('The simple iteration method \n')
    solution_I, error_I, iterations_I, x_k_list_I = sim.simple_iteration(matrix, vector_b, eps, max_iteration)
    if error_I:
        print('The method of simple iteration is divergent')
    else:
        print('The solution of the system is {}'.format(solution_I))
        print('The number of iterations is {}'.format(iterations_I))
        print('The error of the solution is {}'.format(matrix.dot(solution_I) - vector_b))
        #print('The list of x_k')
        #print(x_k_list_I)
    print('\n')
    print('The Gauss-Zeidel method \n')
    solution_GZ, error_GZ, iterations_GZ, x_k_list_GZ = GZ.Gauss_Zeidel(matrix, vector_b, eps, max_iteration)
    if error_GZ:
        print('The Gauss-Zeidel method is divergent')
    else:
        print('The solution of the system is {}'.format(solution_GZ))
        print('The number of iterations is {}'.format(iterations_GZ))
        print('The error of the solution is {}'.format(matrix.dot(solution_GZ) - vector_b))
        # print('The list of x_k')
        # print(x_k_list_GZ)
    print('\n')


    print('The solution with libraries is {}'.format(np.linalg.solve(matrix, vector_b)))
    print('The erorr of library solution is {}'.format(matrix.dot(np.linalg.solve(matrix, vector_b)) - vector_b))

