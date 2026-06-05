# 5. Однофамильцы
# Читаем количество сотрудников
n = int(input())
# Словарь для подсчёта фамилий
counts = {}
for _ in range(n):
    surname = input()
    counts[surname] = counts.get(surname, 0) + 1
# Суммируем количество людей с повторяющимися фамилиями
total = 0
for c in counts.values():
    if c > 1:
        total += c
print(total)
