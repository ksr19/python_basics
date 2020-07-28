try:
    with open("text_1.txt", "r", encoding='utf-8') as f:
        content = f.readlines()
        print(f"В файле {f.name} {len(content)} строк.")
        for i, el in enumerate(content, 1):
            print(f"Количество слов в строке {i}: {len(el.split())}")
except IOError:
    print("Отсутствует файл 'text_1.txt'")
