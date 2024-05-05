import numpy as np

A = np.zeros([1], dtype=np.complex64)
real = np.array([1], dtype=np.complex64)
imag = np.array([1], dtype=np.complex64)

imag = imag * np.sqrt(-1, dtype=np.complex64)

A = real + imag
print(A)