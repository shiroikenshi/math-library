# math-library-project/math_library/combinatorics.py

def factorial(n):
    """Retorna o fatorial de n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combination(n, k):
    """Retorna o número de combinações de n itens tomados k a k."""
    if n < k:
        raise ValueError("n must be greater than or equal to k")
    return factorial(n) // (factorial(k) * factorial(n - k))

def permutation(n, k):
    """Retorna o número de permutações de n itens tomados k a k."""
    if n < k:
        raise ValueError("n must be greater than or equal to k")
    return factorial(n) // factorial(n - k)