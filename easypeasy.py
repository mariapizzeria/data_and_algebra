import numpy as np

a = np.array([
    [1, 3, 0, 2],
    [-5, 16, 4, 0],
    [2, -3, 8, 1],
    [7, 1, -4, 0]
])
w, v = np.linalg.eig(a)
print("Eigenvalues:") #собственные значения
print(w)
print("Eigenvectors:") #собственные векторы
print(v)