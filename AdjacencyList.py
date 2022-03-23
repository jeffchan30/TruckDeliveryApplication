import csv

# Creates an adjacency list with the street address as the vertices. Miles represent the edges.
class AdjacenyList:

    # Initializes a list of miles and locations

    def __init__(self):
        self.locationDictionary = {}
        self.truckMiles = {}

    # Vertex is added to the dictionary with address as key
    def vertex_to_dictionary(self, vertex):
        self.locationDictionary[vertex] = []

    # Loads packages to dictionary as a vertex
    # Complexity of O(N^2)
    def load_packages_to_dictionary(self, hash_table):
        for slot in hash_table.ht:
            for entry in slot:
                self.locationDictionary[entry[1]].append(entry)

    # The miles of trucks represent the edges
    def add_truck_weight(self, vertex_1, vertex_2, truck_miles=1):
        self.truckMiles[(vertex_1, vertex_2)] = truck_miles


# Reads WGUPS_Distance_Table.csv
# Complexity of O(N)
def read_wgups_distance_table(file):
    wgups_distance_table_csv = []
    with open(file) as wgups_distance_table_csv_file:
        reader = csv.reader(wgups_distance_table_csv_file)
        next(reader, None)
        for row in reader:
            wgups_distance_table_csv.append(row)
    return wgups_distance_table_csv


# Creates a hash table
# Complexity of O(N^2)
def get_hash_table(file):
    distance_table_data = read_wgups_distance_table(file)
    adjacency_list_distances = AdjacenyList()
    for row in distance_table_data:
        adjacency_list_distances.vertex_to_dictionary(row[1])
    for row in distance_table_data:
        for i in range(3, len(row)):
            adjacency_list_distances.add_truck_weight(row[1], distance_table_data[i - 3][1], float(row[i]))
    return adjacency_list_distances

adjacencyList = get_hash_table("WGUPS_Distance_Table.csv")