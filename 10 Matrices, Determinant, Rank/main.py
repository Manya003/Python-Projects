import numpy as np

matrix = np.array([[1, 2], [3, 4]])

det = np.linalg.det(matrix)
rank = np.linalg.matrix_rank(matrix)

print("Determinant:", det)
print("Rank:", rank)