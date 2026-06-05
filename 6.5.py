n = int(input("Количество сотрудников: "))
counts = {}
for i in range(n):
    surname = input(f"Фамилия {i+1}: ")
    counts[surname] = counts.get(surname, 0) + 1
total = 0
for c in counts.values():
    if c > 1:
        total += c
print("Количество однофамильцев:", total)
