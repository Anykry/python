class Stationery:
    title = ''

    def draw(self):
        print('отрисовка')


class Pen(Stationery):

    def draw(self):
        print('Вы пишите ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Вы рисуете карандашом')


class Handle(Stationery):

    def draw(self):
        print('Выделяем маркером')

my_pen = Pen()
my_pen.title = 'Ручка Андрея'
my_pen.draw()
print(my_pen.title)

my_pencil = Pencil()
my_pencil.title = 'Карандаш Андрея'
my_pencil.draw()
print(my_pencil.title)

my_highlighter = Handle()
my_highlighter.title = 'Красный маркер'
my_highlighter.draw()
print(my_highlighter.title)