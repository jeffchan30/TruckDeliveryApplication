import csv


# This is the hash table class
class HashTable:

    # Hash table is initialized
    # Complexity of O(N)
    def __init__(self, buckets=8):
        self.ht = []
        for i in range(buckets):
            self.ht.append([])

        # Function to remove a package
        # Complexity of O(N)

    def remove_pckg(self, hash_key):

        slot = hash(hash_key) % len(self.ht)
        slot_list = self.ht[slot]

        for wgups_pckg in slot_list:
            if wgups_pckg[0] == hash_key:
                slot_list.remove(hash_key)

    # Look-up function for packages
    # Complexity of O(N)
    def lookup_pckg(self, hash_key):

        slot = hash_key % len(self.ht)
        slot_list = self.ht[slot]

        for wgups_pckg in slot_list:
            if wgups_pckg[0] == hash_key:
                return wgups_pckg

    # Inserts package into hash table
    # Complexity of O(1)
    def insert_pckg(self, hash_key, wgups_pckg):
        wgups_pckg[0] = int(wgups_pckg[0])
        bucket = hash_key % len(self.ht)
        self.ht[bucket].append(wgups_pckg)
        if wgups_pckg[7] != "9:05":
            wgups_pckg.append("At the hub")
        if wgups_pckg[7] == "9:05":
            wgups_pckg.append("Delayed")


# Gets data from package file and enters it to the hash table
# Complexity of O(N)
def get_pckg(file):
    packages_to_hashtable = HashTable()
    with open(file) as wgups_package_file:
        reader = csv.reader(wgups_package_file)
        next(reader, None)
        for row in reader:
            packages_to_hashtable.insert_pckg(int(row[0]), row)
    return packages_to_hashtable


# Initializes hash table
init_pckg_ht = get_pckg("WGUPS_Package_File.csv")

# Prints package info
def lookup_pckg_info(id):
    info = init_pckg_ht.lookup_pckg(id)
    print(info)
