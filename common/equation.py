import matrix_expression as me
import initialization
import numpy as np

# Расчёт значений узловых потенциалов всей схемы
def U(A, Y, I, E):
    LEFT = me.matrix_multiplication(A, Y)
    LEFT = me.matrix_multiplication(LEFT, me.transposition(A))

    RIGHT = me.matrix_multiplication(Y, E)
    RIGHT = me.addition(I, RIGHT)
    RIGHT = me.matrix_multiplication(A, RIGHT)
    RIGHT = me.scalar_multiplication(-1, RIGHT)

    matrix = me.gauss(LEFT, RIGHT)

    rowcount = matrix.shape[0]

    list = np.zeros([rowcount + 1], dtype=np.complex64)
    for i in range(1, rowcount + 1):
        list[i] = matrix[i - 1, 0]

    dictionary = {
        'list':list,
        'matrix':matrix
    }

    return dictionary

# Расчёт значений узловых потенциалов в точках X
def X():
    U_list = U()['list']

    list = np.zeros([10 + 1], dtype=np.complex64)

    list[ 1] = U_list[15]
    list[ 2] = U_list[11]
    list[ 3] = U_list[ 9]
    list[ 4] = U_list[10]
    list[ 5] = U_list[ 7]
    list[ 6] = U_list[ 8]
    list[ 7] = U_list[ 3]
    list[ 8] = U_list[ 4]
    list[ 9] = U_list[ 1]
    list[10] = U_list[ 2]

    dictionary = {
        'list':list
    }

    return dictionary