# math-library-project/math_library/statistic_functions.py

def mean(numbers):
    """Calcula a média de uma lista de números."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calcula a mediana de uma lista de números."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def mode(numbers):
    """Calcula a moda de uma lista de números."""
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    return [num for num, count in counts.items() if count == max_count]

def standard_deviation(numbers):
    """Calcula o desvio padrão de uma lista de números."""
    mean_value = mean(numbers)
    variance = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5