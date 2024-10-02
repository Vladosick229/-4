n = int(input("Введите число: "))
divisible_by_5 = [x for x in range(1, n + 1) if x % 5 == 0]
print(divisible_by_5)