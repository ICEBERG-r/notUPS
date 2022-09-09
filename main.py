# Mark Wilson
# Student ID:  010314264
import csv


class HashHashBaby:
    def __init__(self, initial_capacity=20):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, item):
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        bucket_list.append(item)

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            print('Item is not found')
            return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                   self.zip_code, self.deadline, self.weight, self.status)


def load_packages(filename):
    with open(filename) as packages:
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
            p_status = "Loaded"

            package = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_status)

            myHash.insert(p_id, package)


myHash = HashHashBaby()

load_packages('packages.csv')
