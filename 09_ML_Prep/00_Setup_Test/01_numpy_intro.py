import numpy as np

# Scalar
scalar = np.array(5)
print("Scalar:", scalar, "Shape:", scalar.shape)

# Vector
vector = np.array([1, 2, 3])
print("Vector:", vector, "Shape:", vector.shape)

# Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix, "\nShape:", matrix.shape)

# Dot Product
dot = np.dot(vector, np.array([4, 5, 6]))
print("Dot Product:", dot)