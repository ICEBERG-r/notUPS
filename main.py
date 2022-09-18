# Mark Wilson
# Student ID:  010314264
import csv


class HashHashBaby:
    def __init__(self, initial_capacity=64):
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

        # for kv in bucket_list:
        #   if kv[0] == key:
        #      return kv[1]
        # return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


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
        for package in package_data:
            p_id = package[0]
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zip = package[4]
            p_deadline = package[5]
            p_weight = package[6]
            p_status = "Loaded"

            p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_status)

            myHash.insert(p_id, p)


myHash = HashHashBaby()

load_packages('packages.csv')

for k in range(len(myHash.table)):
    print("Package: {}".format(myHash.search(k)))
