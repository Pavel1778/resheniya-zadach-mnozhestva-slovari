s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
common = set(s1) & set(s2)
print("Общие символы:", ''.join(common))
