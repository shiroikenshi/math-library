# math-library/linear_algebra.py

import numpy as np

def dot_product(vector1, vector2):
    """Calcula o produto escalar entre dois vetores."""
    return np.dot(vector1, vector2)

def cross_product(vector1, vector2):
    """Calcula o produto vetorial entre dois vetores."""
    return np.cross(vector1, vector2)

def matrix_multiply(matrix1, matrix2):
    """Multiplica duas matrizes."""
    return np.matmul(matrix1, matrix2)

def determinant(matrix):
    """Calcula o determinante de uma matriz."""
    return np.linalg.det(matrix)

def trace(matrix):
    """Calcula o traço de uma matriz."""
    return np.trace(matrix)

def solve_linear_system(coefficients, constants):
    """Resolve um sistema de equações lineares."""
    return np.linalg.solve(coefficients, constants)