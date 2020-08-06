class Date:
    def __init__(self, string_date):
        self.string_date = string_date
        if type(self.parse_date(string_date)) != str:
            self.day, self.month, self.year = self.parse_date(string_date)
        else:
            self.day = self.month = self.year = None

    def __str__(self):
        if self.day and self.month and self.year:
            return f'День - {self.day}, Месяц - {self.month}, Год - {self.year}.'
        else:
            return self.parse_date(self.string_date)

    @classmethod
    def parse_date(cls, string_date):
        try:
            day, month, year = map(int, string_date.split("-"))
            cls.validate(day, month, year)
            return [day, month, year]
        except ValueError:
            return 'Дата должна быть указана числами в формате "день-месяц-год"!'
        except InputException as err:
            return err.text

    @staticmethod
    def validate(day, month, year):
        if day > 31 or day < 1 or month > 12 or month < 1 or year > 9999 or year < 1000:
            raise InputException('Неверный формат даты!')


class InputException(Exception):
    def __init__(self, text):
        self.text = text


d1 = Date('21-03-2020')
print(d1)
d2 = Date('str-01-2010')
print(d2)
d3 = Date('45-91-2030')
print(d3)
