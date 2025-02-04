# Создайте класс House.
# Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

# метод go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".

    def go_to(self,new_floor):
        #nf = [i for i in range(1, new_floor+1)] # генератор списка для создания произвольного списка целых чисел
        nf = list(range(1, new_floor+1))
        if new_floor > self.number_of_floors:
           print("Такого этажа не существует")
        else:
            print(*nf[:], sep="\n") # вывод строки в виде столбца

 #print(*nf[:], new_floor) - выводится как строка


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)







