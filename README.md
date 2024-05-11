# Math Library

A simple math library for performing arithmetic operations, complex number operations, mathematical functions, linear algebra, geometry, and statistics.

## Installation

You can install the math_library package using pip:

```terminal
pip install git+https://github.com/shiroikenshi/math_library.git
```

## Usage

```python
import math_library

# Example usage of arithmetic operations
result_addition = math_library.add(3, 5)
result_subtraction = math_library.subtract(10, 4)
result_multiplication = math_library.multiply(2, 6)
result_division = math_library.divide(8, 2)

# Example usage of complex numbers
complex_num1 = math_library.ComplexNumber(3, 2)
complex_num2 = math_library.ComplexNumber(1, -1)
result_complex_addition = complex_num1 + complex_num2
result_complex_subtraction = complex_num1 - complex_num2
result_complex_multiplication = complex_num1 * complex_num2
result_complex_division = complex_num1 / complex_num2

# Example usage of mathematical functions
result_sin = math_library.sin(math.pi/2)
result_cos = math_library.cos(math.pi)
result_tan = math_library.tan(math.pi/4)
result_log = math_library.log(10, 2)
result_exp = math_library.exp(2)

# Example usage of linear algebra functions
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result_dot_product = math_library.dot_product(vector1, vector2)
result_cross_product = math_library.cross_product(vector1, vector2)

# Example usage of geometry functions
result_area_square = math_library.area_square(5)
result_perimeter_square = math_library.perimeter_square(5)

# Example usage of statistics functions
data = [1, 2, 3, 4, 5]
result_mean = math_library.mean(data)
result_median = math_library.median(data)
result_mode = math_library.mode(data)
result_std_deviation = math_library.standard_deviation(data)
```

## Documentation

For detailed documentation and examples, please refer to the documentation.

## Contributing

Contributions are welcome! Please read our contribution guidelines for details.

## License

This project is licensed under the MIT License - see the LICENSE file for details.