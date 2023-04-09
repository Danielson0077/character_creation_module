from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления\n '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    square = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {square}')


print(message)
calc(25.5)
