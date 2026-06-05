# 2. Символическая разница
# Читаем две строки
s1 = input()
s2 = input()
# Пересечение множеств
common = set(s1) & set(s2)
print(''.join(common))
