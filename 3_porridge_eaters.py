# 3. Кашееды
# Читаем количество детей
n = int(input())
m = int(input())
# Множества фамилий
manna = set()
for _ in range(n):
    manna.add(input())
oatmeal = set()
for _ in range(m):
    oatmeal.add(input())
# Пересечение
both = manna & oatmeal
count = len(both)
if count == 0:
    print("Таких нет")
else:
    print(count)
