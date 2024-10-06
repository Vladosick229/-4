numbers = list(map(int, input("Введите числа через пробел: ").split()))

# Создание нового списка с квадратами чисел
squares = [number**2 for number in numbers]

# Вывод результата
print(squares)