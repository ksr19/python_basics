import json

try:
    with open('text_7.txt', 'r', encoding='utf-8') as f:
        firm_profit = {line.split()[0]: round((float(line.split()[2]) - float(line.split()[3])), 2) for line in f}
        profits = [value for value in firm_profit.values() if value >= 0]
        firm_details = [firm_profit, {'average_profit': round(sum(profits) / len(profits), 2)}]

    with open('text_7.json', 'w', encoding='utf-8') as f:
        json.dump(firm_details, f, indent=4, ensure_ascii=False)
except IOError:
    print("Отсутствует файл 'text_7.txt'")
