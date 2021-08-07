class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Your speed is: {self.speed}')

    def go(self):
        print('The car is GO!')

    def stop(self):
        print('The car is STOP!')

    def turn(self, direction):
        print('The car is turn to the: ' + direction)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Exceed speed limit for town car - 60 km/h')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Exceed speed limit for work car - 40 km/h')

my_car = WorkCar(50, 'red', 'Mazda', False)

my_car.show_speed()
my_car.go()
my_car.stop()
print(my_car.name)
print(my_car.is_police)

police = Car(90, 'white', 'Porshe', True)

police.show_speed()
print(police.name)
print(police.is_police)

police.go()
police.stop()
police.turn('left')
