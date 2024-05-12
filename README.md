# <div align="center"><a href="/README.md">Português</a> | <a href="/README_EN.md">Inglês</a></div>
<br><br>

# Math Library

Uma biblioteca de matemática simples para realizar operações aritméticas, operações com números complexos, funções matemáticas, álgebra linear, geometria e estatísticas.

## Instalação

Você pode instalar o pacote math_library usando o pip:

```terminal
pip install git+https://github.com/shiroikenshi/math-library-project.git
```

## Uso

```python
import math_library

# Exemplo de uso de operações aritméticas
result_addition = math_library.add(3, 5)
result_subtraction = math_library.subtract(10, 4)
result_multiplication = math_library.multiply(2, 6)
result_division = math_library.divide(8, 2)

# Exemplo de uso de números complexos
complex_num1 = math_library.ComplexNumber(3, 2)
complex_num2 = math_library.ComplexNumber(1, -1)
result_complex_addition = complex_num1 + complex_num2
result_complex_subtraction = complex_num1 - complex_num2
result_complex_multiplication = complex_num1 * complex_num2
result_complex_division = complex_num1 / complex_num2

# Exemplo de uso de funções matemáticas
result_sin = math_library.sin(math.pi/2)
result_cos = math_library.cos(math.pi)
result_tan = math_library.tan(math.pi/4)
result_log = math_library.log(10, 2)
result_exp = math_library.exp(2)

# Exemplo de uso de funções de álgebra linear
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result_dot_product = math_library.dot_product(vector1, vector2)
result_cross_product = math_library.cross_product(vector1, vector2)

# Exemplo de uso de funções de geometria
result_area_square = math_library.area_square(5)
result_perimeter_square = math_library.perimeter_square(5)

# Exemplo de uso de funções de estatísticas
data = [1, 2, 3, 4, 5]
result_mean = math_library.mean(data)
result_median = math_library.median(data)
result_mode = math_library.mode(data)
result_std_deviation = math_library.standard_deviation(data)
```

## Documentação

Para documentação detalhada e exemplos, consulte a documentação.

## Contribuindo

Contribuições são bem-vindas! Por favor, leia nossas diretrizes de contribuição para mais detalhes.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.