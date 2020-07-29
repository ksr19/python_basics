class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника {self.name} {self.surname}.")

    def get_total_income(self):
        print(f"Полный доход сотрудника составляет {self._income['wage'] + self._income['bonus']}.")


worker_1 = Position("Андрей", "Леонидов", "продавец", 100, 25)
worker_2 = Position("Леонид", "Андреев", "менеджер", 200, 50)
worker_3 = Position("Павел", "Сергеев", "инженер", 130)
for worker in [worker_1, worker_2, worker_3]:
    print(f"Сотрудник {worker.name} {worker.surname} занимает позицию {worker.position.title()} и "
          f"имеет следующую структуру доходов {worker._income}.")
    worker.get_full_name()
    worker.get_total_income()
