# math_library/arithmetic.py

def add(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtract(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def multiply(a, b):
    """Retorna o produto de dois números."""
    return a * b

def divide(a, b):
    """Retorna o quociente da divisão de dois números."""
    if b == 0:
        return float('inf')
    return a / b

def power(base, exponent):
    """Retorna a base elevada ao expoente."""
    return base ** exponent

def square_root(number):
    """Retorna a raiz quadrada de um número."""
    if number < 0:
        raise ValueError("Square root of negative number is not defined")
    return number ** 0.5

def modulo(a, b):
    """Retorna o resto da divisão de a por b."""
    return a % b

def integer_division(a, b):
    """Retorna a parte inteira da divisão de a por b."""
    return a // b

def minimum(a, b):
    """Retorna o menor de dois números."""
    return min(a, b)

def maximum(a, b):
    """Retorna o maior de dois números."""
    return max(a, b)

def round_number(number, decimal_places=0):
    """Arredonda um número para um número específico de casas decimais."""
    return round(number, decimal_places)