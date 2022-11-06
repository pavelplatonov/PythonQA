# 5.1.  Создайте любой класс с произвольным количеством подклассов,
#       экземпляров, атрибутов и методов
#       -   как минимум один атрибут должен быть с уровнем доступа private.
#           Соответственно, для получания значений этого атрибута
#           нужно использовать методы get и set


from os import name


class Employee:  # класс сотрудники
    """Базовый класс для всех сотрудников"""

    emp_count = 0  # счётчик сотрудников

    def __init__(self, name, salary, hours):  # функция добавления нового сотрудника
        self.name = name  # аргумент класса имя
        self.salary = salary  # аргумент класса зарплата
        self.hours = hours  # аргумент класса с параметром часы
        Employee.emp_count += 1  # команда на увеличение счётчика сотрудников

    def display_count(
        self,
    ):  # метод класса с выводом текста в определенном формате
        # и счётчиком сотрудников
        print("Всего сотрудников: %d" % Employee.emp_count)

    def display_employee(self):
        print(
            "Имя: {}. Зарплата: {}. Количество рабочих часов: {}".format(
                self.name, self.salary, self.hours
            )
        )


# Это создаст первый объект класса Employee
emp1 = Employee("Андрей", 2000, 12)
# Это создаст второй объект класса Employee
emp2 = Employee("Мария", 5000, 8)
# Это создаст третий объект класса Employee
emp3 = Employee("Павел", 8000, 6)
# вывод параметров объекта emp1 и emp2 при помощи метода display_employee
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
print("Всего сотрудников: %d" % Employee.emp_count)


class tovar:  # Создаём класс товар
    """Базовый класс для всех товаров"""

    tovar_count = 0

    def __init__(self, artikul, name, ves, sklad):
        self.artikul = artikul
        self.__name = name
        self.ves = ves
        self.sklad = sklad
        tovar.tovar_count += 1

    def display_count(
        self,
    ):
        print("На складе осталось %d товаров" % tovar.tovar_count)

    def display_pozicia(self):
        print(
            "Позиция с артикулом {}, наименованием {}, весом {}, на складе {}".format(
                self.artikul, self.__name, self.ves, self.sklad
            )
        )

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name


tort_praga = tovar("00112", "Praga", "1200gr", "Kond.ceh")
tort_mars = tovar("00113", "Marsel", "700gr", "Kond.ceh")

tort_mars.display_pozicia()
tort_praga.display_pozicia()

print("На складе имеется %d товара" % tovar.tovar_count)
# 5.2.  Cоздайте репозиторий на Github и отправте файл с домашним заданием
#       в этот удаленный репозиторий
