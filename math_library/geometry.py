# math-library-project/math_library/geometry.py

def area_square(side):
    """Calcula a área de um quadrado."""
    return side ** 2

def perimeter_square(side):
    """Calcula o perímetro de um quadrado."""
    return 4 * side

def area_rectangle(length, width):
    """Calcula a área de um retângulo."""
    return length * width

def perimeter_rectangle(length, width):
    """Calcula o perímetro de um retângulo."""
    return 2 * (length + width)