number = int(input("Введите число: "))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print(f"Факториал числа {number} равен {factorial}")