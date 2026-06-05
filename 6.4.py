replace = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}
text = input("Введите русский текст: ")
result = []
for ch in text:
    low = ch.lower()
    if low in replace:
        repl = replace[low]
        if ch.isupper():
            repl = repl[0].upper() + repl[1:]
        result.append(repl)
    elif low in ('ъ', 'ь'):
        continue
    else:
        result.append(ch)
print("Транслитерация:", ''.join(result))
