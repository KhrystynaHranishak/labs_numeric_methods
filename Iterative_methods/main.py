import input
import output


EPS = 0.001 # the accuracy of solution
MAX_ITERATIONS = 1000

#user_matrix, user_b = input.get_data_keyboard()
#output.print_out(user_matrix, user_b, EPS, MAX_ITERATIONS)

A_test, c_test = input.test_data()
output.print_out(A_test, c_test, EPS, MAX_ITERATIONS)

A_exp, c_exp = input.file_data()
output.print_out(A_exp, c_exp, EPS, MAX_ITERATIONS)



