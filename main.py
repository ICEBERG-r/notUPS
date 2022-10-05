# Mark Wilson
# Student ID:  010314264
import csv
import datetime


# Hash-map - copied from lecture, may need to add functions or make more original
class HashMap:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, time_of_delivery):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.time_of_delivery = time_of_delivery

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                       self.zip_code, self.deadline, self.weight, self.status,
                                                       self.time_of_delivery)

    def __repr__(self):
        return str(self)


class Truck:
    def __init__(self):
        self.mph = 18.0
        self.payload = []
        self.time = 8.0
        self.mileage = 0.0
        self.sorted_payload = []
        self.current_location = 0


def load_packages(filename):
    with open(filename, encoding="utf-8") as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zip = package[4]
            p_deadline = package[5]
            p_weight = package[6]
            p_notes = package[7]
            p_status = "At Hub"
            p_time_of_delivery = None

            p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_notes, p_status,
                        p_time_of_delivery)

            if p.package_id == 9:
                p.address = "410 S State St"
                p.zip_code = "84111"

            if p.package_id in {1, 2, 8, 13, 14, 15, 16, 20, 21, 27, 30, 34, 35, 39, 40}:
                truck_1.payload.append(p)

            if p.package_id in {3, 5, 6, 7, 12, 18, 25, 26, 29, 31, 32, 36, 37, 38}:
                truck_2.payload.append(p)

            if p.package_id in {4, 9, 10, 11, 17, 19, 22, 23, 24, 28, 33}:
                truck_3.payload.append(p)

            package_hash.insert(p_id, p)


def load_addresses(filename):
    with open(filename, encoding='utf-8-sig') as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        for address in address_data:
            loc_id = int(address[0])
            loc_address = address[1]

            address_lookup[loc_address] = loc_id


def get_distance(loc_1, loc_2):
    return float(distance_table[loc_1][loc_2])


def convert_float_time_to_hm(time_float):
    return str(datetime.timedelta(hours=time_float))[:-3]


def convert_hm_time_to_float(time_hms):
    pass


def get_min_distance(truck, location):
    min_distance = 9000.0
    for p in range(len(truck.payload)):
        if get_distance(location, address_lookup.get(truck.payload[p].address)) <= min_distance:
            min_distance = get_distance(location, address_lookup.get(truck.payload[p].address))

    return min_distance


'''
def get_next_package(truck, location):
    min_distance = 9000.0
    package_index = None
    for p in range(len(truck.payload)):
        if get_distance(location, address_lookup.get(truck.payload[p].address)) <= min_distance:
            min_distance = get_distance(location, address_lookup.get(truck.payload[p].address))
            package_index = p

    return package_index
'''
'''
def get_next_location(truck, location):
    min_distance = 9000.0
    next_location = 0
    for p in range(len(truck.payload)):
        if get_distance(location, address_lookup.get(truck.payload[p].address)) <= min_distance:
            min_distance = get_distance(location, address_lookup.get(truck.payload[p].address))
            next_location = address_lookup.get(truck.payload[p].address)

    return next_location
'''


def get_total_mileage():
    total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage
    return total_mileage


def deliver_packages(truck):
    current_location = 0
    while len(truck.payload) != 0:

        min_distance = 9000.0
        package_index = None
        next_location = None

        for p in range(len(truck.payload)):

            (package_hash.search(truck.payload[p].package_id)).status = 'In Transit'
            if get_distance(current_location, address_lookup.get(truck.payload[p].address)) <= min_distance:
                min_distance = get_distance(current_location, address_lookup.get(truck.payload[p].address))
                next_location = address_lookup.get(truck.payload[p].address)
                package_index = p

        current_location = next_location
        (package_hash.search(truck.payload[package_index].package_id)).status = 'Delivered'
        truck.time += (min_distance/truck.mph)
        (package_hash.search(truck.payload[package_index].package_id)).time_of_delivery = truck.time
        truck.mileage += min_distance
        truck.payload.pop(package_index)

    truck.mileage += get_distance(current_location, 0)
    truck.time += (get_distance(current_location, 0)/truck.mph)


package_hash = HashMap()

address_lookup = {}

truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()

truck_2.time = 9.10
truck_3.time = 10.5


distance_table = list(csv.reader(open('distance.csv', encoding='utf-8-sig')))


load_packages('packages.csv')
load_addresses('address.csv')


deliver_packages(truck_1)
deliver_packages(truck_2)
deliver_packages(truck_3)

print("hello") #DELETE THIS
print(convert_float_time_to_hm(truck_1.time))
print(convert_float_time_to_hm(truck_2.time))
print(convert_float_time_to_hm(truck_3.time))

print(get_total_mileage())

for i in range(1, 40):
    print(package_hash.search(i))

'''
class Main:
    def __init__(self):
        pass

    print('Welcome to WGUPS package tracking')
    print('All deliveries were completed in ', "{0:.2f}".format(get_total_mileage(), 2), 'miles.')
    print('Please enter a number from the following menu')
    start = input('1 - Package lookup \n2 - View status of all packages at a specific time \n0 - exit the program')
    
    while start != 0:
        if start == 1:
            try:
                p_id = input('Enter the package ID: ')
'''
# This is how you can convert a float to a time
# x = 3.6
# print(str(datetime.timedelta(hours=x))[:-3])
