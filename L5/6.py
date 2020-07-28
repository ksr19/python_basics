import re

with open("text_6.txt", encoding='utf-8') as f:
    courses_info = {re.findall('[a-zA-zа-яА-Я]+', line)[0]: sum(map(int, re.findall('[0-9]+', line))) for line in f}
    print(courses_info)
