# Описание задания:
# Класс Warehouse - склад. В программе создается экземпляр класса - brovary_store
# Класс в виде словаря словарей хранит такую структуру - экземпляр техники, отдел, количество
# Методы класса:
# getbalance - возвращает остаток количества экземпляра техники в указанном отделе
# receipt - увеличивает количество экземпляра техники в указанном отделе
# move_to - уменьшает количество экземпляра техники в отделе отправителе и увеличивает в отделе получателе
# Класс Tech - потомок для классов Printer и Scanner.
# В первой части программы оздается новый склад brovary_store,
# Вручную создаются несколько экземпляров классов Printer и Scanner, изменяется их состояние в разных отделах на складе
# Во второй части программы эти же действия реализуются через пользовательский ввод -
# Список техники, отделы и количество полностью динамические
# В этом режиме пользователю через консоль предлагается выбрать режим:
#  - создать новый экземпляр техники
#  - выполнить действия с техникой (оприходовать на склад или переместить между складами)
#  - просмотреть список техники
#  - просмотреть состояние (остатков) склада

class Warehouse:
    def __init__(self):
        self.storage = {}

    def getbalance(self, tech, department):
        departments_array = self.storage.get(tech)
        if departments_array is None:
            return 0
        else:
            quantity = departments_array.get(department)
            if quantity is None:
                return 0
            else:
                return quantity

    def action(self, uuid, department, quantity, movement_type):
        balance = self.getbalance(uuid, department)
        if movement_type == 'receipt':
            new_balance = balance + quantity
        else:
            new_balance = balance - quantity

        items_structure = self.storage.get(uuid)
        if items_structure is None:
            self.storage[uuid] = {department: balance + quantity}
        else:
            items_structure.update({department: new_balance})
            self.storage.update({uuid: items_structure})

    def receipt(self, uuid, department, quantity):
        self.action(uuid, department, quantity, 'receipt')

    def moveto(self, uuid, sender, receiver, quantity):
        self.action(uuid, sender, quantity, 'expense')
        self.action(uuid, receiver, quantity, 'receipt')


class CheckValue(Exception):
    def __init__(self, txt):
        self.txt = txt


class Tech:
    manufacturer = ''
    serial = ''
    model = ''
    uuid = ''

    def __str__(self):
        return str(self.model) + ' ' + str(self.manufacturer) + ' ' +str(self.serial)


class Printer(Tech):

    def __init__(self, model, manufacturer, serial, pages_per_minute):
        self.model = model
        self.manufacturer = manufacturer
        self.serial = serial
        self.pages_per_minute = pages_per_minute
        self.uuid = str(model) + str(serial)


class Scanner(Tech):

    def __init__(self, model, manufacturer, serial, time_to_scan):
        self.model = model
        self.manufacturer = manufacturer
        self.serial = serial
        self.time_to_scan = time_to_scan
        self.uuid = str(model) + str(serial)


printer_hp = Printer('LJ 1022', 'Hewlled Packard', 123456, 10)
printer_canon = Printer('LBP 810', 'Canon', 223456, 15)
scanner_epson = Scanner('ES 210', 'EPSON', 1234, 5)
scanner_monilta = Scanner('BZH 264e', 'Konica Minolta', 17234, 5)

print('Our items:')
print(printer_hp.model)
print(scanner_epson.model)
print('-----------------------------')

# Created new Warehouse
brovary_store = Warehouse()

# Put to warehouse our printer hp 5 units to department office
print('Put 5 printers at Office')
brovary_store.receipt(printer_hp, 'Office', 5)

# Check that warehouse filled up correctly
print(brovary_store.storage.get(printer_hp))

# Put to warehouse one more our printer hp 1 unit to department office
print('Put 1 printer at Office')
brovary_store.receipt(printer_hp, 'Office', 1)

# Check that warehouse filled up correctly - it should be 6 printers at the office
print(brovary_store.storage.get(printer_hp))

# Put to warehouse to different department our printer hp 2 unit. The department is Store
print('Put 1 printer at Store')
brovary_store.receipt(printer_hp, 'Store', 1)
brovary_store.receipt(printer_hp, 'Store', 1)

# Check that warehouse filled up correctly - it should be 6 printers at the office and 2 at the Store
print(brovary_store.storage.get(printer_hp))

# Move 1 printer from Store to Office
brovary_store.moveto(printer_hp, 'Store', 'Office', 1)

# Check
print(brovary_store.storage.get(printer_hp))


tech_list = []

def printtechlist():
    for i, el in enumerate(tech_list):
        print(f'{i} - {el}')


def create_new_printer():
    model = input('Enter the model name:')
    manufacturer = input('Enter manufacturer: ')
    serial = input('Enter serial number: ')
    pages = input('Enter print pages per minute: ')
    tech_list.append(Printer(model, manufacturer, serial, pages))


def create_new_scanner():
    model = input('Enter the model name:')
    manufacturer = input('Enter manufacturer: ')
    serial = input('Enter serial number: ')
    time = input('Enter time to scan: ')
    tech_list.append(Printer(model, manufacturer, serial, time))


def create_new_tech():
    if len(tech_list) == 0:
        print('You haven\'n got any tech yet!')
    else:
        print('You current tech list: ', tech_list)
    while True:
        mode = input('1 - Create new printer; 2 - Create new scanner; 0 - exit: ')
        if mode == '0':
            break
        elif mode == '1':
            create_new_printer()
        elif mode == '2':
            create_new_scanner()
        else:
            print('Choose the correct mode 1 or 2 or 0 for exit!')
    if len(tech_list) == 0:
        print('No any tech added!')
    else:
        print('Current list: ')
        printtechlist()


def add_to_warehouse():
    printtechlist()
    if len(tech_list) == 0:
        print('Tech list is empty. Before operations add new tech to the list!')
        return
    item = input('Select the number of Item which you will put to warehouse: ')
    try:
        if not item.isdigit():
            raise CheckValue('Error! Entered value is not an integer!')
    except CheckValue as err:
        print(err)
        add_to_warehouse()
    else:
        item_no = int(item)
    department = input('Enter department name: ')
    quantity = input('Enter quantity: ')
    try:
        if not quantity.isdigit():
            raise CheckValue('Error! Entered value is not an integer!')
    except CheckValue as err:
        print(err)
        return
    else:
        quantity_to_put = int(quantity)
    brovary_store.receipt(tech_list[item_no], department, quantity_to_put)


def move_to_dep():
    printtechlist()
    if len(tech_list) == 0:
        print('Tech list is empty. Before operations add new tech to the list!')
        return
    item = input('Select the position of Item which you will move to: ')
    try:
        if not item.isdigit():
            raise CheckValue('Error! Entered value is not an integer!')
    except CheckValue as err:
        print(err)
        move_to_dep()
    else:
        item_no = int(item)
    sender = input('Enter sender department name: ')
    receiver = input('Enter receiver department name: ')
    quantity = input('Enter quantity: ')
    try:
        if not quantity.isdigit():
            raise CheckValue('Error! Entered value is not an integer!')
    except CheckValue as err:
        print(err)
        return
    else:
        quantity_to_move = int(quantity)
    brovary_store.moveto(tech_list[item_no], sender, receiver, quantity_to_move)


def actions():
    while True:
        input_mode = input('1 - Add tech to warehouse; 2 - move from one department to another; 0 - exit: ')
        if input_mode == '0':
            break
        elif input_mode == '1':
            add_to_warehouse()
        elif input_mode == '2':
            move_to_dep()
        else:
            print('Choose the correct mode 1 or 2 or 0 for exit!')


def warehouse_balance():
    for el in brovary_store.storage:
        print(f'{el} {brovary_store.storage[el]}')


while True:
    mode = input('Select mode: 1 - Create new tech; 2 - Actions with tech; 3 - tech list; 4 - warehouse balance; 0 - exit: ')
    if mode == '0':
        break
    elif mode == '1':
        create_new_tech()
    elif mode == '2':
        actions()
    elif mode == '3':
        printtechlist()
    elif mode == '4':
        warehouse_balance()
    else:
        print('Choose the correct mode 1 or 2 or 3 or 4 or 0 for exit!')
