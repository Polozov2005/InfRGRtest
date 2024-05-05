import pandas as pd # Для чтения Excell таблиц
import numpy as np # Для создания матриц

# Инициализация списка источников ЭДС из файла E.xlsx
def E():
    filepath = 'excell_tables/E.xlsx'
    df = pd.read_excel(filepath)
    rowcount = df.shape[0]
    matrix = np.zeros([rowcount + 1], dtype=np.complex64)
    for i in range(1, rowcount + 1):
        matrix[i] = df.iloc[i - 1, 1]
    return(matrix)

# Инициализация списка значений проводимости из файла Y.xlsx
def Y():
    filepath = 'excell_tables/Y.xlsx'
    df = pd.read_excel(filepath)
    print(df)
    rowcount = df.shape[0]
    matrix = np.zeros([rowcount + 1], dtype=np.complex64)
    real = np.zeros([rowcount + 1], dtype=np.complex64)
    imag = np.zeros([rowcount + 1], dtype=np.complex64)
    for i in range(1, rowcount + 1):
        real[i] = df.iloc[i - 1, 1]
    for i in range(1, rowcount + 1):
        imag[i] = df.iloc[i - 1, 2]
    imag = imag * np.sqrt(-1, dtype=np.complex64)
    matrix = real + imag
    return matrix

