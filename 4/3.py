numbers = [4, 11, 15, 7, 20, 3, 12]
max_number = numbers[0]
i = 1

while i < len(numbers):
    if numbers[i] > max_number:
        max_number = numbers[i]
    i += 1

print(f"Максимальное число в списке: {max_number}")