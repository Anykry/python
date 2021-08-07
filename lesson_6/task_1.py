import time


class TrafficLight:
    __color = 'red'
    color_time = {'red': 7, 'yellow': 2, 'green': 5}

    def __init__(self):
        print('Traffic light is running')

    def running(self, color):
        if color == 'yellow' and TrafficLight.__color != 'red':
            print('Incorrect state. The Yellow could be only after Red')
            return
        elif color == 'green' and TrafficLight.__color != 'yellow':
            print('Incorrect state. The Green could be only after Yellow')
            return

        TrafficLight.__color = color

        wait_time = TrafficLight.color_time.get(TrafficLight.__color)

        print(f'{TrafficLight.__color} - wait {wait_time} seconds')
        time.sleep(wait_time)


my_trafficlight = TrafficLight()

my_trafficlight.running('red')
my_trafficlight.running('yellow')
my_trafficlight.running('green')