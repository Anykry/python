class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, sqare_meter_mass, thikness):
        mass = self._length * self._width * sqare_meter_mass * thikness
        return mass

road = Road(5000, 20) # ширину и длину дороги передаем в конструктор

print(f"The total mass is: {road.calculate_mass(25, 5)} kg") # масса покрытия асфальта 1см, число покрытия в см задаем при вызове метода
