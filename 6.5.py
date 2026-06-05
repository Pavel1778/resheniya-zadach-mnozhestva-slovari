# Задание 5 "Однофамильцы"
n = int(input("Количество сотрудников: "))
counts = {}
for i in range(n):
    s = input(f"Фамилия {i+1}: ")
    counts[s] = counts.get(s, 0) + 1
total = 0
for c in counts.values():
    if c > 1:
        total += c
print("Количество однофамильцев:", total)
