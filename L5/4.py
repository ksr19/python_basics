from googletrans import Translator

try:
    with open("text_4.txt", "r") as i_f:
        with open("new_text_4.txt", "w") as o_f:
            for line in i_f:
                translation = Translator().translate(line[:line.index('-') - 1], dest='ru', src='en')
                o_f.write(translation.text.capitalize() + line[line.index('-') - 1:])
except IOError:
    print("Отсутствует файл 'text_4.txt'")
