numbers = [4, 11, 15, 7, 20, 3, 12]
count = 0

for number in numbers:
    if number > 10:
        count += 1

print(f"Количество чисел, больших 10: {count}")