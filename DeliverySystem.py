from Truck import insert_packages_and_get_optimal_route, truck_two, status, total_truck_miles, dispatch_trucks, truck_three
from Hashtable import lookup_pckg_info
from Algo import dijkstra

# This is the user interface
def delivery_system():

    #Menu
    choose_option = input("Choose a command \n"
                         "Press 'D' - Deliver packages \n"
                         "Press 'L' - Look up packages \n")

    # Search package
    if choose_option == "L" or choose_option == "l":
        packageID = input("Enter ID of package to search: ")
        lookup_pckg_info(int(packageID))
        delivery_system()

    # Inserts packages
    if choose_option == "D" or choose_option == "d":
        insert_packages_and_get_optimal_route()
        _835_status = input("Press 'S' for a status update between 8:35 AM and 9:25 AM")

        if _835_status == "S" or _835_status == "s":
            status(9, 25, 0)
            print("")
            address_update = input("WARNING! Package #9's address is incorrect. Press 'U' to update the address for Package #9" )

            if address_update == "U" or address_update == "u":
                print("Address updated")
                for wgups_pckg in truck_two.package_on_truck:
                    if wgups_pckg[7] == "Wrong address listed":
                        truck_two.remove_pckg(wgups_pckg)
                for wgups_pckg in truck_two.package_on_truck:
                    if wgups_pckg[0] == 8:
                        wgups_pckg[8] = 'Package has been delivered'

                # Package and route is updated
                address_updated = ['9', '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD', '2', 'Wrong address listed', 'Will be delivered soon']
                truck_two.insert_pckg(address_updated)
                truck_two.delivery_route = dijkstra(truck_two.delivery_route)
                truck_two.delivery_route.append("HUB")

                # Status for 9:35 AM - 10:25AM
                _935_status = input("Press 'S' for status update between 9:35 AM and 10:25 AM")

                if _935_status == "S" or _935_status == "s":
                    status(10, 25, 0)
                    _1203_status = input("Press 'S' for status update between 12:03 PM and 13:12 PM")

                    # Status for 12:03 PM
                    if _1203_status == "S" or _1203_status == "s":
                        status(13, 12, 0)
                        total_status = input("Press 'S' to for status update of all deliveries and truck miles")

                        # Status after delivery
                        if total_status == "S" or total_status == "s":
                            dispatch_trucks()
                            total_truck_miles()
                            print("Trucks One, Two, and Three delivered all the packages and returned to hub at: ", truck_three.delivery_complete.time())
                            SystemExit
