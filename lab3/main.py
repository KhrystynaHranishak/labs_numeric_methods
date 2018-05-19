import  sys
import numpy as np
import my_input
import Jaccobi_method as JM

EPS = sys.float_info.epsilon

A_1 = my_input.test_2()
val_matrix_1, T_list_1 = JM.Jaccobi_method(A_1.copy(), EPS)
Q_1 = JM.find_vectors(T_list_1)

print('Initial matrix \n {}'.format(A_1))
print('A matrix with values on a diagonal \n {}'.format(val_matrix_1))
print('A matrix with vectors \n {}'.format(Q_1))

print('Check')
Q_1T = np.transpose(Q_1)
#print(Q_1T)
print(Q_1T.dot(Q_1))
print('\n')
x = np.matmul(Q_1, val_matrix_1)
print(x.dot(Q_1T) - A_1)

# Додати виведення сліду, послідовності максимальних елементів та норми матриць через бібліотеку linalg.norm(''frob)
