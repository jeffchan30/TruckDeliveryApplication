from AdjacencyList import adjacencyList


# Dijkstra's algorithm is used to find the optimal path.
# Complexity of O(N^2)
def dijkstra(shortest_route):
    starting_address = "HUB"
    sort_truck_routes = shortest_route
    hash_table_truck_miles = adjacencyList.truckMiles
    dijkstra_algorithm = [starting_address]
    while len(sort_truck_routes) != 0:
        minimum_distance = [0, starting_address]
        for node in sort_truck_routes:
            route_dist = hash_table_truck_miles[dijkstra_algorithm[-1], node]
            if minimum_distance[0] == 0:
                minimum_distance = [route_dist, node]
            if route_dist < minimum_distance[0] and route_dist != 0:
                minimum_distance = [route_dist, node]
        if minimum_distance[1] not in dijkstra_algorithm:
            dijkstra_algorithm.append(minimum_distance[1])
        sort_truck_routes.remove(minimum_distance[1])
    return dijkstra_algorithm