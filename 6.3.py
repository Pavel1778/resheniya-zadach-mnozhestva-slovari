# Задание 3 "Кашееды"
n = int(input("Сколько детей любят манную кашу? "))
manna = set()
for i in range(n):
    manna.add(input(f"Фамилия {i+1}: "))
m = int(input("Сколько детей любят овсяную кашу? "))
oatmeal = set()
for i in range(m):
    oatmeal.add(input(f"Фамилия {i+1}: "))
both = manna & oatmeal
if len(both) == 0:
    print("Таких нет")
else:
    print("Количество детей, любящих обе каши:", len(both))
