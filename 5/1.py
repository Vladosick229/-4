num = int(input("Введите число: "))
is_prime = True
i = 2

if num < 2:
    is_prime = False
else:
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{num} является простым числом")
else:
    print(f"{num} не является простым числом")