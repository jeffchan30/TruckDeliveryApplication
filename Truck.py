from Algo import dijkstra
from AdjacencyList import adjacencyList
from datetime import datetime, timedelta
from Hashtable import init_pckg_ht

# Truck class
class Truck:

    # Initializes the truck with package, time, route, and miles
    def __init__(self):
        self.miles_per_minute = 0.3
        self.time_now = None
        self.package_on_truck = []
        self.delivery_route = []
        self.delivery_start = None
        self.delivery_complete = None

    # Load packages
    def insert_pckg(self, pckg):
        self.package_on_truck.append(pckg)
        self.delivery_route.append(pckg[1])

    # Removes packages after delivery
    def remove_pckg(self, pckg):
        self.package_on_truck.remove(pckg)
        self.delivery_route.remove(pckg[1])

    # Time when the truck is back at the hub
    def back_at_hub(self, hub_time):
        self.delivery_complete = hub_time
        return hub_time

    # Time after delivery
    def time_of_delivery(self, delivered_time):
        self.time_now = delivered_time
        return delivered_time

    # Starts delivery
    def start_delivering_package(self, start_time):
        self.delivery_start = start_time





# Creates a list of locations
locations_list = []

# Truck objects
truck_one = Truck()
truck_two = Truck()
truck_three = Truck()


# Store packages in to the dictionary
adjacencyList.load_packages_to_dictionary(init_pckg_ht)

# Insert packages into trucks and gets optimal route
# Complexity is O(N^2)

def insert_packages_and_get_optimal_route():

    # Inserts addresses into the adjacency list
    for unvisited_address in adjacencyList.locationDictionary:
        locations_list.append(unvisited_address)

    # Inserts packages that need to be delivered by 9:00 AM
    for locations in locations_list:
        for wgups_pckg in adjacencyList.locationDictionary[locations]:
            if wgups_pckg[5] == "9:00 AM":
                truck_one.insert_pckg(wgups_pckg)


    # Inserts packages that need to be delivered by 10:30 AM and is delayed
    for locations in locations_list:
        for wgups_pckg in adjacencyList.locationDictionary[locations]:
            if wgups_pckg[7] != "" and wgups_pckg[7] != "Can only be on truck 2" and wgups_pckg[7] != "Delayed on flight---will not arrive to depot until 9:05 am" and wgups_pckg[7] != "Wrong address listed" and  wgups_pckg[5] == "10:30 AM":
                truck_one.insert_pckg(wgups_pckg)
            if wgups_pckg[7] == "Delayed on flight---will not arrive to depot until 9:05 am" and wgups_pckg[5] == "10:30 AM":
                truck_two.insert_pckg(wgups_pckg)

    # Inserts packages that need to be delivered by 10:30 AM and no notes
    for locations in locations_list:
        for wgups_pckg in adjacencyList.locationDictionary[locations]:
            if wgups_pckg[7] == "" and wgups_pckg[5] == "10:30 AM":
                truck_one.insert_pckg(wgups_pckg)

    # Inserts packages that need to be delivered by the end of the day that are can only be delivered by truck 2, wrong
    # address or delayed
    for locations in locations_list:
        for wgups_pckg in adjacencyList.locationDictionary[locations]:
            if wgups_pckg[5] == "EOD" and wgups_pckg[7] == "Wrong address listed":
                truck_two.insert_pckg(wgups_pckg)
            if wgups_pckg[5] == "EOD" and wgups_pckg[7] == "Can only be on truck 2":
                truck_two.insert_pckg(wgups_pckg)
            if wgups_pckg[5] == "EOD" and wgups_pckg[7] == "Delayed on flight---will not arrive to depot until 9:05 am":
                truck_two.insert_pckg(wgups_pckg)


    # Packages that need to be delivered by the end of the day and over 16 packages
    for locations in locations_list:
        for wgups_pckg in adjacencyList.locationDictionary[locations]:
            if wgups_pckg[7] == "" and wgups_pckg[5] == "EOD":
                if len(truck_one.package_on_truck) < 16:
                    truck_one.insert_pckg(wgups_pckg)
                elif len(truck_two.package_on_truck) < 16:
                    truck_two.insert_pckg(wgups_pckg)
                elif len(truck_three.package_on_truck) < 16:
                    truck_three.insert_pckg(wgups_pckg)



    # Trucks will travel via optimal route
    truck_one.delivery_route = dijkstra(truck_one.delivery_route)
    truck_two.delivery_route = dijkstra(truck_two.delivery_route)
    truck_three.delivery_route = dijkstra(truck_three.delivery_route)

    # Trucks will return back to the hub
    truck_one.delivery_route.append("HUB")
    truck_two.delivery_route.append("HUB")
    truck_three.delivery_route.append("HUB")

    print("Trucks have begun delivery.")

# Gets miles for each truck
# Complexity is O(N)
def truck_miles(course):
    weight = adjacencyList.truckMiles
    miles = 0
    for i in range(0, len(course) - 1):
        miles = miles + weight[course[i], course[i + 1]]
    return miles


# Gets trucks' total miles
# Complexity is O(N)
def total_truck_miles():
    truck_one_miles = truck_miles(truck_one.delivery_route)
    truck_two_miles = truck_miles(truck_two.delivery_route)
    truck_three_miles = truck_miles(truck_three.delivery_route)
    total_miles = truck_one_miles + truck_two_miles + truck_three_miles

    print("Truck One Total Distance: " + str(round(truck_one_miles, 2)))
    print("----------------------------------------")
    print("Truck Two Total Distance: " + str(round(truck_two_miles, 2)))
    print("----------------------------------------")
    print("Truck Three Total Distance: " + str(round(truck_three_miles,2)))
    print("----------------------------------------")
    print("Total miles travelled: " + str(round(total_miles, 2)))

# Add seconds to get correct time
# Complexity is O(1)
def seconds_util(time, seconds):
    date_time = datetime(1, 1, 1, time.hour, time.minute, time.second)
    date_time = date_time + timedelta(seconds = seconds)
    return date_time.time()


# Dispatches trucks to addresses
# Complexity is O(N^2)
def dispatch_trucks():
    miles_bet_addresses = adjacencyList.truckMiles

    truck_one_dispatch = datetime(2021, 5, 12, 8, 0, 0)
    truck_one.delivery_start = truck_one_dispatch
    truck_one.time_now = truck_one_dispatch
    for i in range(0, len(truck_one.delivery_route) - 1):
        dist_between_routes = miles_bet_addresses[truck_one.delivery_route[i], truck_one.delivery_route[i + 1]]
        miles_per_minute = truck_one.miles_per_minute
        minutes = dist_between_routes / miles_per_minute
        add_seconds = round(minutes * 60, 2)
        time_of_delivery = seconds_util(truck_one.time_now, add_seconds)
        truck_one.time_now = datetime(2021, 5, 12, time_of_delivery.hour, time_of_delivery.minute, time_of_delivery.second)
        status_update_of_delivery = "Package has been delivered @ " + str(time_of_delivery)
        for wgups_pckg in truck_one.package_on_truck:
            if truck_one.delivery_route[i + 1] == wgups_pckg[1]:
                wgups_pckg[8] = status_update_of_delivery
    truck_one.delivery_complete = truck_one.time_now
    print("Truck One Information: ", *truck_one.package_on_truck, sep="\n")

    truck_two_dispatch = datetime(2021, 5, 12, 1, 1, 1)
    truck_two.delivery_start = truck_two_dispatch
    truck_two.time_now = truck_two_dispatch
    for i in range(0, len(truck_two.delivery_route) - 1):
        dist_between_routes = miles_bet_addresses[truck_two.delivery_route[i], truck_two.delivery_route[i + 1]]
        miles_per_minute = truck_two.miles_per_minute
        minutes = dist_between_routes / miles_per_minute
        add_seconds = round(minutes * 60, 2)
        time_of_delivery = seconds_util(truck_two.time_now, add_seconds)
        truck_two.time_now = datetime(2021, 5, 12, time_of_delivery.hour, time_of_delivery.minute, time_of_delivery.second)
        status_update_of_delivery = "Package has been delivered @ " + str(time_of_delivery)
        for wgups_pckg in truck_two.package_on_truck:
            if truck_two.delivery_route[i + 1] == wgups_pckg[1]:
                wgups_pckg[8] = status_update_of_delivery
    truck_two.delivery_complete = truck_two.time_now
    print("")
    print("")
    print("Truck Two Information: ", *truck_two.package_on_truck, sep="\n")

    truck3_start = truck_one.delivery_complete
    truck_three.delivery_start = truck3_start
    truck_three.time_now = truck3_start
    for i in range(0, len(truck_three.delivery_route) - 1):
        dist_between_routes = miles_bet_addresses[truck_three.delivery_route[i], truck_three.delivery_route[i + 1]]
        miles_per_minute = truck_three.miles_per_minute
        minutes = dist_between_routes / miles_per_minute
        add_seconds = round(minutes * 60, 2)
        time_of_delivery = seconds_util(truck_three.time_now, add_seconds)
        truck_three.time_now = datetime(2021, 5, 12, time_of_delivery.hour, time_of_delivery.minute, time_of_delivery.second)
        status_update_of_delivery = "Package has been delivered @ " + str(time_of_delivery)
        for wgups_pckg in truck_three.package_on_truck:
            if truck_three.delivery_route[i + 1] == wgups_pckg[1]:
                wgups_pckg[8] = status_update_of_delivery
    truck_three.delivery_complete = truck_three.time_now

    print("")
    print("")
    print("Truck Three Information: ", *truck_three.package_on_truck, sep="\n")

# Sets delivery status to "en route"
# Complexity is O(N)
def en_route(package_on_truck):
    for wgups_pckg in package_on_truck:
        wgups_pckg[8] = "en route"

# Sees package status at different times
# Complexity is O(N^2)
def status(hour, minute, second):
    miles_bet_addresses = adjacencyList.truckMiles
    time_at_stop = datetime(2021, 5, 12, hour, minute, second)

    truck_one_dispatch = datetime(2021, 5, 12, 8, 0, 0)
    truck_one.delivery_start = truck_one_dispatch
    truck_one.time_now = truck_one_dispatch
    en_route(truck_one.package_on_truck)
    for i in range(0, len(truck_one.delivery_route) - 1):
        dist_between_routes = miles_bet_addresses[truck_one.delivery_route[i], truck_one.delivery_route[i + 1]]
        miles_per_minute = truck_one.miles_per_minute
        minutes = dist_between_routes / miles_per_minute
        add_seconds = round(minutes * 60, 2)
        time_of_delivery = seconds_util(truck_one.time_now, add_seconds)
        if time_of_delivery < time_at_stop.time():
            truck_one.time_now = datetime(2021, 5, 12, time_of_delivery.hour, time_of_delivery.minute, time_of_delivery.second)
            status_update_of_delivery = "Package has been delivered @ " +  str(time_of_delivery)
            for wgups_pckg in truck_one.package_on_truck:
                if truck_one.delivery_route[i + 1] == wgups_pckg[1]:
                    wgups_pckg[8] = status_update_of_delivery
    truck_one.delivery_complete = truck_one.time_now
    print("Truck One Information:", *truck_one.package_on_truck, sep="\n")

    truck_two_dispatch = datetime(2021, 5, 12, 9, 5, 0)
    truck_two.delivery_start = truck_two_dispatch
    truck_two.time_now = truck_two_dispatch
    en_route(truck_two.package_on_truck)
    for i in range(0, len(truck_two.delivery_route) - 1):
        dist_between_routes = miles_bet_addresses[truck_two.delivery_route[i], truck_two.delivery_route[i + 1]]
        miles_per_minute = truck_two.miles_per_minute
        minutes = dist_between_routes / miles_per_minute
        seconds_to_add = round(minutes * 60, 2)
        time_of_delivery = seconds_util(truck_two.time_now, seconds_to_add)
        if time_of_delivery < time_at_stop.time():
            truck_two.time_now = datetime(2021, 5, 12, time_of_delivery.hour, time_of_delivery.minute, time_of_delivery.second)
            status_update_of_delivery = "Package has been delivered @ " + str(time_of_delivery)
            for wgups_pckg in truck_two.package_on_truck:
                if truck_two.delivery_route[i + 1] == wgups_pckg[1]:
                    wgups_pckg[8] = status_update_of_delivery
    truck_two.delivery_complete = truck_two.time_now
    print("")
    print("")
    print("Truck Two Information:", *truck_two.package_on_truck, sep="\n")

    truck_three_dispatch = truck_one.delivery_complete
    truck_three.delivery_start = truck_three_dispatch
    truck_three.time_now = truck_three_dispatch
    en_route(truck_three.package_on_truck)
    for i in range(0, len(truck_three.delivery_route) - 1):
        dist_between_routes = miles_bet_addresses[truck_three.delivery_route[i], truck_three.delivery_route[i + 1]]
        miles_per_minute = truck_three.miles_per_minute
        minutes = dist_between_routes / miles_per_minute
        seconds_to_add = round(minutes * 60, 2)
        time_of_delivery = seconds_util(truck_three.time_now, seconds_to_add)
        if time_of_delivery < time_at_stop.time():
            truck_three.time_now = datetime(2020, 5, 12, time_of_delivery.hour, time_of_delivery.minute, time_of_delivery.second)
            status_update_of_delivery = "Package has been delivered @ " + str(time_of_delivery)
            for wgups_pckg in truck_three.package_on_truck:
                if truck_three.delivery_route[i + 1] == wgups_pckg[1]:
                    wgups_pckg[8] = status_update_of_delivery
    truck_three.delivery_complete = truck_three.time_now
    print("")
    print("")
    print("Truck Three Information:", *truck_three.package_on_truck, sep="\n")