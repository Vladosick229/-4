n = int(input("Введите число: "))
product = 1

for i in range(1, n + 1):
    product *= i

print(f"Произведение всех чисел от 1 до {n} равно {product}")
