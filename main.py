# Mark Wilson
# Student ID:  010314264

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


myHash = HashHashBaby()
myHash.insert('Hello World')
print(myHash.table)

print(myHash.search('Hello World'))
