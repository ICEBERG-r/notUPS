# Mark Wilson
# Student ID:  010314264
import csv
import datetime
import operator


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
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                   self.zip_code, self.deadline, self.weight, self.status)

    def __repr__(self):
        return str(self)


class Truck:
    def __init__(self):
        self.mph = 18.0
        self.payload = []
        self.start_time = 8.0
        self.mileage = 0.0
        self.has_driver = False


class Vertex:
    def __init__(self, loc_id, label):
        self.loc_id = loc_id
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

    def __str__(self):
        return "%s, %s" % (self.loc_id, self.label)

    def __repr__(self):
        return str(self)


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


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

            p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_notes, p_status)

            if p.package_id in {1, 2, 13, 14, 15, 16, 20, 21, 27, 34, 35, 39, 40}:
                truck_1.payload.append(p)

            if p.package_id in {3, 5, 6, 7, 8, 12, 18, 25, 26, 29, 30, 31, 32, 36, 37, 38}:
                truck_2.payload.append(p)

            if p.package_id in {4, 9, 10, 11, 17, 19, 22, 23, 24, 28, 33}:
                truck_3.payload.append(p)

            packageHash.insert(p_id, p)


def load_addresses(filename):
    with open(filename, encoding='utf-8-sig') as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        for address in address_data:
            loc_id = int(address[0])
            loc_address = address[1]

            address_lookup[loc_address] = loc_id

            v = Vertex(loc_id, loc_address)
            vertex_array.append(v)


def get_distance(loc_1, loc_2):
    if str(distance_table[loc_1][loc_2]) == '':
        return distance_table[loc_2][loc_1]
    else:
        return distance_table[loc_1][loc_2]


'''
def dijkstra(g, start_vertex):
    unvisited = []
    for current_vertex in g.adjacency_list:
        unvisited.append(current_vertex)

    start_vertex.distance = 0

    while len(unvisited) > 0:
        min_index = 0
        for i in range(1, len(unvisited)):
            if unvisited[i].distance < unvisited[min_index].distance:
                min_index = i
        current_vertex = unvisited.pop(min_index)

        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alt_path_distance = current_vertex.distance + edge_weight

            if alt_path_distance < adj_vertex.distance:
                adj_vertex.distance = alt_path_distance
                adj_vertex.pred_vertex = current_vertex
'''

'''
def get_shortest_path(start_vertex, end_vertex):
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = ' -> ' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
'''

packageHash = HashMap()

truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()

g = Graph()

address_lookup = {}
vertex_array = []
distance_table = list(csv.reader(open('distance.csv', encoding='utf-8-sig')))


for n in vertex_array:
    g.add_vertex(vertex_array[n])

for n in vertex_array:
    g.add_undirected_edge(vertex_array[n], vertex_array[n+1], float(distance_table[n][n+1]))

load_packages('packages.csv')
load_addresses('address_vertex.csv')

print(truck_1.payload)
print(truck_2.payload)
print(truck_3.payload)

print(get_distance(0, 4))
# print(float(distance_table[7][3]))

# print(packageHash.search(30))

# print(truck_1)
# print(truck_2)
# print(truck_3)

# may not implement dijkstra, a greedy algorithm would be easier to implement
# dijkstra(g, vertex_array[0])

# for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
#    if v.pred_vertex is None and v is not vertex_array[0]:
#        print("HUB to %s: no path exists" % v.label)
#    else:
#        print("HUB to %s: %s (total weight: g)" % (v.label, get_shortest_path(vertex_array[0], v), v.distance))

# This is how you can convert a float to a time
# x = 3.6
# print(str(datetime.timedelta(hours=x))[:-3])


