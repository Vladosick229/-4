num = [4, 11, 15, 7, 20, 3, 12]
max_num = num[0]
i = 1

while i < len(num):
    if num[i] > max_num:
        max_num = num[i]
    i += 1

print(f"Максимальное число в списке: {max_num}")