# math-library-project/math_library/complex_numbers.py

class ComplexNumber:
    def __init__(self, real, imag):
        """Inicializa um número complexo com parte real e imaginária."""
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        """Soma dois números complexos."""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Subtrai dois números complexos."""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """Multiplica dois números complexos."""
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __truediv__(self, other):
        """Divide dois números complexos."""
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)
    
    def __abs__(self):
        """Retorna o módulo de um número complexo."""
        return (self.real**2 + self.imag**2) ** 0.5
    
    def __str__(self):
        """Retorna uma representação em string do número complexo."""
        return f"{self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i"