import numpy as np


def file_data():
    A = [[9.1, 5.6, 7.8], [3.8, 5.1, 2.8], [4.1, 5.7, 1.2]]
    b = [9.8, 6.7, 5.8]
    return np.array(A), np.array(b)

def test_data():
    A = [[100., 6., -2.], [6., 200., -10.], [1., -2., -100.]]
    b = [200., 600., 500.]
    return np.array(A), np.array(b)

def get_data_keyboard():
    error = True
    while error:
        try:
            rows_number = int(input('Input the number of rows:'))
            columns_number = int(input('Input the number of columns:'))
            print('\n' + 'The size of matrix is ' + str(rows_number) + ' x ' + str(columns_number) + '\n')

            matrix = []
            while (rows_number != 0):
                row = input('Input the row of the matrix as a separator use space:')
                row = row.split(' ')
                row = [float(x) for x in row]
                matrix.append(row)
                rows_number = rows_number - 1

            vector_b = []
            row = input('Input the vector b as a separator use space:')
            row = row.split(' ')
            vector_b = [float(x) for x in row]
            error = False

            #print('\n' + 'The matrix A is:')
            #print(matrix)
            #print('\n' + 'The vector b is:')
            #print(vector_b)

        except ValueError:
            error = True
            print("Incorrent format. Try again")
    return matrix, vector_b