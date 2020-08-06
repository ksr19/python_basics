class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'День - {self.date[0]}, Месяц - {self.date[1]}, Год - {self.date[2]}.'

    @classmethod
    def parse_date(cls, string_date):
        try:
            day, month, year = map(int, string_date.split("-"))
            date = [day, month, year]
            cls.validate(date)
            return cls(date)
        except ValueError:
            return 'Дата должна быть указана числами в формате "день-месяц-год"!'
        except InputException as err:
            return err

    @staticmethod
    def validate(date):
        if date[0] > 31 or date[0] < 1 or date[1] > 12 or date[1] < 1 or date[2] > 9999 or date[2] < 1000:
            raise InputException('Неверный формат даты!')


class InputException(Exception):
    def __init__(self, text):
        self.text = text


d1 = Date.parse_date('21-03-2020')
print(d1)
d2 = Date.parse_date('str-01-2010')
print(d2)
d3 = Date.parse_date('45-91-2030')
print(d3)
