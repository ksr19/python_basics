def get_input(input_text):
    # Получение начальных запасов по товарам.
    while True:
        try:
            amount = int(input(input_text))
            if amount < 0:
                raise StockError("Величина должна быть целым неотрицательным числом!")
            else:
                break
        except (ValueError, StockError):
            print("Величина должна быть целым неотрицательным числом!")
    return amount


def get_answer(input_text, max_number):
    # Выбор варианта из меню действий.
    while True:
        try:
            amount = int(input(input_text))
            if amount < 1 or amount > max_number:
                raise StockError("Выберите один из предложенных вариантов, указав соответствующую цифру!")
            else:
                break
        except (ValueError, StockError):
            print("Выберите один из предложенных вариантов, указав соответствующую цифру!")
    return amount


class Warehouse:
    def __init__(self, printer, scanner, xerox):
        self.__stock = {'printer': printer, 'scanner': scanner, 'xerox': xerox}

    def __str__(self):
        return f"\nНа складе находится:\n\u00B7Принтеры - {self.__stock['printer']} шт." \
               f"\n\u00B7Сканеры - {self.__stock['scanner']} шт." \
               f"\n\u00B7Ксероксы - {self.__stock['xerox']} шт."

    def __add__(self, other):
        return Warehouse(self.__stock['printer'] + other.__stock['printer'],
                         self.__stock['scanner'] + other.__stock['scanner'],
                         self.__stock['xerox'] + other.__stock['xerox'])

    def __sub__(self, other):
        return Warehouse(self.__stock['printer'] - other.__stock['printer'],
                         self.__stock['scanner'] - other.__stock['scanner'],
                         self.__stock['xerox'] - other.__stock['xerox'])

    def stock_up(self, printer, scanner, xerox):
        # Пополнение запасов.
        return self + Warehouse(printer, scanner, xerox)

    def stock_down(self, division, printer, scanner, xerox):
        # Отгрузка товаров в департамент division.
        self.__validate((self - Warehouse(printer, scanner, xerox)).__stock, division)
        print(f"В отдел {division} отправлены:\n\u00B7Принтеры - {printer} шт."
              f"\n\u00B7Сканеры - {scanner} шт."
              f"\n\u00B7Ксероксы - {xerox} шт."
              )
        return self - Warehouse(printer, scanner, xerox)

    @staticmethod
    def __validate(stock_dict, div_name):
        # Проверка достаточности запасов на складе.
        problem_hardware = []
        for key, value in stock_dict.items():
            if value < 0:
                problem_hardware.append(key)
        if problem_hardware:
            raise StockError(f"Отгрузка в отдел {div_name} не может быть произведена. "
                             f"На складе недостаточно следующих типов оргтехники:"
                             f"{Warehouse.__translate(problem_hardware)}!")

    @staticmethod
    def __translate(key_list):
        # Создание строки для уточнения товаров, по которым недостаточно запасов на складе.
        output_phrase = ""
        for i in range(len(key_list)):
            if key_list[i] == 'printer':
                output_phrase += ' принтер,'
            elif key_list[i] == 'scanner':
                output_phrase += ' сканер,'
            else:
                output_phrase += ' ксерокс,'
            if i == len(key_list) - 1:
                output_phrase = output_phrase[:-1]
        return output_phrase

    @property
    def printer(self):
        return self.__stock['printer']

    @property
    def scanner(self):
        return self.__stock['scanner']

    @property
    def xerox(self):
        return self.__stock['xerox']


class Hardware:
    def __init__(self, price, weight, manufacturer, model, output_speed, resolution):
        self.price = price
        self.weight = weight
        self.manufacturer = manufacturer
        self.model = model
        self.output_speed = output_speed
        self.resolution = resolution


class Printer(Hardware):
    def __init__(self, price, weight, manufacturer, model, output_speed, resolution, toner, time_delay, pcl_number,
                 airprint=False):
        super().__init__(price, weight, manufacturer, model, output_speed, resolution)
        self.toner = toner
        self.time_delay = time_delay
        self.airprint = airprint
        self.pcl_number = pcl_number

    def __str__(self):
        return f"\nПринтер {self.manufacturer} {self.model}:\n\u00B7Масса - {self.weight} кг." \
               f"\n\u00B7Необходимый тонер - {self.toner}." \
               f"\n\u00B7Скорость работы - {self.output_speed} страниц в минуту." \
               f"\n\u00B7Максимальное разрешение - {self.resolution}x{self.resolution} dpi. " \
               f"\n\u00B7Время выхода первого отпечатка - {self.time_delay} сек." \
               f"\n\u00B7Количество установленных шрифтов PCL - {self.pcl_number}. " \
               f"\n\u00B7Поддержка AirPrint - {'Есть' if self.airprint else 'Отсутствует'}. " \
               f"\n\u00B7Оптовая цена - {self.price} рублей."


class Scanner(Hardware):
    def __init__(self, price, weight, manufacturer, model, output_speed, resolution, scan_format, color_depth,
                 sensor):
        super().__init__(price, weight, manufacturer, model, output_speed, resolution)
        self.scan_format = scan_format
        self.color_depth = color_depth
        self.sensor = sensor

    def __str__(self):
        return f"\nСканер {self.manufacturer} {self.model}:\n\u00B7Масса - {self.weight} кг." \
               f"\n\u00B7Скорость работы - {self.output_speed} страниц в минуту." \
               f"\n\u00B7Максимальное разрешение - {self.resolution}x{self.resolution} dpi. " \
               f"\n\u00B7Формат сканирования - {self.scan_format}." \
               f"\n\u00B7Глубина цвета - {self.color_depth} бит. " \
               f"\n\u00B7Тип датчика - {self.sensor}. " \
               f"\n\u00B7Оптовая цена - {self.price} рублей."


class Xerox(Hardware):
    def __init__(self, price, weight, manufacturer, model, output_speed, resolution, toner, time_delay):
        super().__init__(price, weight, manufacturer, model, output_speed, resolution)
        self.toner = toner
        self.time_delay = time_delay

    def __str__(self):
        return f"\nКсерокс {self.manufacturer} {self.model}:\n\u00B7Масса - {self.weight} кг." \
               f"\n\u00B7Необходимый тонер - {self.toner}." \
               f"\n\u00B7Скорость работы - {self.output_speed} страниц в минуту." \
               f"\n\u00B7Максимальное разрешение - {self.resolution}x{self.resolution} dpi. " \
               f"\n\u00B7Время выхода первого отпечатка - {self.time_delay} сек." \
               f"\n\u00B7Оптовая цена - {self.price} рублей."


class StockError(Exception):
    def __init__(self, message):
        self.message = message


p = Printer(5000, 8, 'Lexmark', 'B3340dw', 38, 1200, 'High Yield Unison', 5, 89, False)
s = Scanner(4500, 2, 'Canon', 'LiDE400', 480, 4800, 'многостраничный PDF', 48, 'CIS')
x = Xerox(2500, 1.8, 'Xerox', '3025BI', 20, 600, '106R03048', 10)
print(f"Доступная оргтехника:\n1.{p}\n2.{s}\n3.{x}\n")
printer_amount = get_input("Введите начальный остаток принтеров на складе: ")
scanner_amount = get_input("Введите начальный остаток сканеров на складе: ")
xerox_amount = get_input("Введите начальный остаток ксероксов на складе: ")
w = Warehouse(printer_amount, scanner_amount, xerox_amount)
print(f"Суммарная стоимость товаров на складе: "
      f"{p.price * printer_amount + s.price * scanner_amount + x.price * xerox_amount} рублей.")
print(w)
while True:
    answer = get_answer("Выберите операцию, которую вы хотите произвести:\n"
                        "1 -- Текущее состояние склада;\n"
                        "2 -- Пополнение запасов склада;\n"
                        "3 -- Отгрузка товаров в отдел;\n"
                        "4 -- Вернуть товары на склад;\n"
                        "5 -- Прекращение взаимодействия.\n", 5)
    if answer == 1:
        print(f"Стоимость товаров на складе: "
              f"{p.price * w.printer + s.price * w.scanner + x.price * w.xerox} рублей.")
        print(w)

    if answer == 2:
        printer_amount = get_input("Введите количество приобретенных принтеров: ")
        scanner_amount = get_input("Введите количество приобретенных сканеров: ")
        xerox_amount = get_input("Введите количество приобретенных ксероксов: ")
        w = Warehouse.stock_up(w, printer_amount, scanner_amount, xerox_amount)
        print(f"Суммарная стоимость приобретенных товаров: "
              f"{p.price * printer_amount + s.price * scanner_amount + x.price * xerox_amount} рублей.")
        print(w)

    if answer == 3:
        division = input("Введите название подразделения, куда необходимо произвести отгрузку: ")
        printer_amount = get_input("Введите количество отгружаемых принтеров: ")
        scanner_amount = get_input("Введите количество отгружаемых сканеров: ")
        xerox_amount = get_input("Введите количество отгружаемых ксероксов: ")
        try:
            w = Warehouse.stock_down(w, division, printer_amount, scanner_amount, xerox_amount)
        except StockError as err:
            print(err)
        print(w)

    if answer == 4:
        printer_amount = get_input("Введите количество возвращенных принтеров: ")
        scanner_amount = get_input("Введите количество возвращенных сканеров: ")
        xerox_amount = get_input("Введите количество возвращенных ксероксов: ")
        w = Warehouse.stock_up(w, printer_amount, scanner_amount, xerox_amount)
        print(w)

    if answer == 5:
        break
