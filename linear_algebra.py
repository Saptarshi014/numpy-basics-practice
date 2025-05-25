import numpy as np

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)
print("Matrix Multiplication:\n", result)

# Determinant
det = np.linalg.det(matrix1)
print("Determinant:", det)

# Inverse
inverse = np.linalg.inv(matrix1)
print("Inverse Matrix:\n", inverse)

# Eigenvalues and eigenvectors