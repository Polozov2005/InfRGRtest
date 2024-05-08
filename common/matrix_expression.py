import numpy as np # Для создания матриц

# Сложение матриц
def addition(A, B):
    if A.shape != B.shape:
        print('Ошибка при сложении: матрицы должны быть одного размера')
    else:
        C = np.copy(A)
        C = C.astype('complex64')

        D = np.copy(B)
        D = D.astype('complex64')

        rowcount = C.shape[0]
        columncount = C.shape[1]

        result = np.zeros([rowcount, columncount], dtype=np.complex64)

        for i in range(rowcount):
            for j in range(columncount):
                result[i, j] = C[i, j] + D[i, j]

        return result

# Умножение матриц
def multiplication(A, B):
    if A.shape[1] != B.shape[0]:
        print('Ошибка при умножении: число столбцов первого множителя должно совпадать', 
              'с числом строк второго множителя')   
    else:
        C = np.copy(A)
        C = C.astype('complex64')

        D = np.copy(B)
        D = D.astype('complex64')

        rowcount = C.shape[0]
        columncount = D.shape[1]

        result = np.zeros([rowcount, columncount], dtype=np.complex64)

        for i in range(rowcount):
            for k in range(columncount):
                for j in range(C.shape[1]):
                    result[i, k] = result[i, k] + C[i, j] * B[j, k]

        return result

# Транспонирование
def transposition(A):
    T = np.copy(A)
    T = T.astype('complex64')

    rowcount = T.shape[1]
    columncount = T.shape[0]

    result = np.zeros([rowcount, columncount], dtype=np.complex64)

    for i in range(rowcount):
        for j in range(columncount):
            result[i, j] = T[j, i]

    return result

A = np.array([
    [1, 1],
    [1, 1],
    [1, 1],
    [1, 1],

])

B = np.array([
    [2],
    [2]
])

C = transposition(A)
print(C)