class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


emploee = Position('Ivan', 'Jakovlev', 'director', 100, 50)

# Проверяем работу метода
print(emploee.get_full_name())

print(emploee.get_total_income())

# Проверяем значение публичного атрибута
print(emploee.name)

# Проверяем значение защищенного атрибута
print(emploee._income)