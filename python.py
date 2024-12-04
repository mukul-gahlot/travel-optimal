class DistanceGraph:
    def __init__(self, cities):
        self.cities = cities
        self.city_index = {}
        
        # Create the city_index dictionary
        for i, city in enumerate(cities):
            self.city_index[city] = i
        
        # Initialize the graph as a 2D list
        self.graph = []
        for i in range(len(cities)):
            row = []
            for j in range(len(cities)):
                if i == j:
                    row.append(0)
                else:
                    row.append(float('inf'))
            self.graph.append(row)

    def add_edge(self, city_u, city_v, distance):
        u = self.city_index[city_u]
        v = self.city_index[city_v]
        self.graph[u][v] = distance
        
    def floyd_warshall(self):
        # Copy elements to the distance matrix
        self.dist = []
        for i in range(len(self.graph)):
            temp = []
            for j in range(len(self.graph)):
                temp.append(self.graph[i][j])
            self.dist.append(temp)
            
        # Initialize the next_node matrix for tracking the path
        self.next_node = [[None] * len(self.graph) for _ in range(len(self.graph))]
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] == float('inf'):
                    self.next_node[i][j] = None
                else:
                    self.next_node[i][j] = j
        for k in range(len(self.dist)):
            for i in range(len(self.dist)):
                for j in range(len(self.dist)):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next_node[i][j] = self.next_node[i][k]

    def construct_path(self, u, v):
        if self.next_node[u][v] is None:
            return None
        path = [u]
        while u != v:
            u = self.next_node[u][v]
            path.append(u)
        return path

    def print_path(self, path):
        if path is None:
            print("No path exists")
        else:
            for i in path:
                print(self.cities[i], end=" -> " if i != path[-1] else "")
            print()

    def get_optimal_distance(self, source_city, destination_city):
        source = self.city_index.get(source_city)
        destination = self.city_index.get(destination_city)

        if source is None or destination is None:
            return None, None

        if self.dist[source][destination] == float('inf'):
            return None, None

        path = self.construct_path(source, destination)
        return self.dist[source][destination], path


class PriceGraph:
    def __init__(self, cities):
        self.cities = cities
        self.city_index = {}
        
        # Create the city_index dictionary
        for i, city in enumerate(cities):
            self.city_index[city] = i
        
        # Initialize the graph as a 2D list
        self.graph = []
        for i in range(len(cities)):
            row = []
            for j in range(len(cities)):
                if i == j:
                    row.append(0)
                else:
                    row.append(float('inf'))
            self.graph.append(row)

    def add_edge(self, city_u, city_v, price):
        u = self.city_index[city_u]
        v = self.city_index[city_v]
        self.graph[u][v] = price
        
    def floyd_warshall(self):
        # Copy elements to the distance matrix
        self.dist = []
        for i in range(len(self.graph)):
            temp = []
            for j in range(len(self.graph)):
                temp.append(self.graph[i][j])
            self.dist.append(temp)
            
        # Initialize the next_node matrix for tracking the path
        self.next_node = [[None] * len(self.graph) for _ in range(len(self.graph))]
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] == float('inf'):
                    self.next_node[i][j] = None
                else:
                    self.next_node[i][j] = j
        for k in range(len(self.dist)):
            for i in range(len(self.dist)):
                for j in range(len(self.dist)):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next_node[i][j] = self.next_node[i][k]

    def construct_path(self, u, v):
        if self.next_node[u][v] is None:
            return None
        path = [u]
        while u != v:
            u = self.next_node[u][v]
            path.append(u)
        return path

    def print_path(self, path):
        if path is None:
            print("No path exists")
        else:
            for i in path:
                print(self.cities[i], end=" -> " if i != path[-1] else "")
            print()

    def get_optimal_price(self, source_city, destination_city):
        source = self.city_index.get(source_city)
        destination = self.city_index.get(destination_city)

        if source is None or destination is None:
            return None, None

        if self.dist[source][destination] == float('inf'):
            return None, None

        path = self.construct_path(source, destination)
        return self.dist[source][destination], path


class TimeGraph:
    def __init__(self, cities):
        self.cities = cities
        self.city_index = {}
        
        # Create the city_index dictionary
        for i, city in enumerate(cities):
            self.city_index[city] = i
        
        # Initialize the graph as a 2D list
        self.graph = []
        for i in range(len(cities)):
            row = []
            for j in range(len(cities)):
                if i == j:
                    row.append(0)
                else:
                    row.append(float('inf'))
            self.graph.append(row)

    def add_edge(self, city_u, city_v, time):
        u = self.city_index[city_u]
        v = self.city_index[city_v]
        self.graph[u][v] = time
        
    def floyd_warshall(self):
        # Copy elements to the distance matrix
        self.dist = []
        for i in range(len(self.graph)):
            temp = []
            for j in range(len(self.graph)):
                temp.append(self.graph[i][j])
            self.dist.append(temp)
            
        # Initialize the next_node matrix for tracking the path
        self.next_node = [[None] * len(self.graph) for _ in range(len(self.graph))]
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] == float('inf'):
                    self.next_node[i][j] = None
                else:
                    self.next_node[i][j] = j
        for k in range(len(self.dist)):
            for i in range(len(self.dist)):
                for j in range(len(self.dist)):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next_node[i][j] = self.next_node[i][k]

    def construct_path(self, u, v):
        if self.next_node[u][v] is None:
            return None
        path = [u]
        while u != v:
            u = self.next_node[u][v]
            path.append(u)
        return path

    def print_path(self, path):
        if path is None:
            print("No path exists")
        else:
            for i in path:
                print(self.cities[i], end=" -> " if i != path[-1] else "")
            print()

    def get_optimal_time(self, source_city, destination_city):
        source = self.city_index.get(source_city)
        destination = self.city_index.get(destination_city)

        if source is None or destination is None:
            return None, None

        if self.dist[source][destination] == float('inf'):
            return None, None

        path = self.construct_path(source, destination)
        return self.dist[source][destination], path


def run_distance_program():
    cities = ['delhi', 'mumbai', 'kolkata', 'chennai']
    g = DistanceGraph(cities)
    g.add_edge('delhi', 'mumbai', 5)
    g.add_edge('delhi', 'kolkata', 1)
    g.add_edge('kolkata', 'mumbai', 2)
    g.add_edge('chennai', 'delhi', 1)
    g.add_edge('chennai', 'mumbai', 8)

    g.floyd_warshall()

    source_city = input('Enter source city for distance calculation: ').strip()
    destination_city = input('Enter destination city for distance calculation: ').strip()

    distance, path = g.get_optimal_distance(source_city, destination_city)
    if distance is not None:
        print(f"Shortest distance from {source_city} to {destination_city}: {distance}")
        print(f"Optimal route from {source_city} to {destination_city}:")
        g.print_path(path)
    else:
        print("No path exists or invalid city names entered.")


def run_price_program():
    cities = ['delhi', 'mumbai', 'kolkata', 'chennai']
    g = PriceGraph(cities)
    g.add_edge('delhi', 'mumbai', 100)
    g.add_edge('delhi', 'kolkata', 50)
    g.add_edge('kolkata', 'mumbai', 30)
    g.add_edge('chennai', 'delhi', 60)
    g.add_edge('chennai', 'mumbai', 150)

    g.floyd_warshall()

    source_city = input('Enter source city for price calculation: ').strip()
    destination_city = input('Enter destination city for price calculation: ').strip()

    price, path = g.get_optimal_price(source_city, destination_city)
    if price is not None:
        print(f"Optimal price from {source_city} to {destination_city}: {price}")
        print(f"Optimal route from {source_city} to {destination_city}:")
        g.print_path(path)
    else:
        print("No path exists or invalid city names entered.")


def run_time_program():
    cities = ['delhi', 'mumbai', 'kolkata', 'chennai']
    g = TimeGraph(cities)
    g.add_edge('delhi', 'mumbai', 2)  # Example times
    g.add_edge('delhi', 'kolkata', 1)
    g.add_edge('kolkata', 'mumbai', 3)
    g.add_edge('chennai', 'delhi', 4)
    g.add_edge('chennai', 'mumbai', 5)

    g.floyd_warshall()

    source_city = input('Enter source city for time calculation: ').strip()
    destination_city = input('Enter destination city for time calculation: ').strip()

    time, path = g.get_optimal_time(source_city, destination_city)
    if time is not None:
        print(f"Optimal time from {source_city} to {destination_city}: {time}")
        print(f"Optimal route from {source_city} to {destination_city}:")
        g.print_path(path)
    else:
        print("No path exists or invalid city names entered.")


if __name__ == "__main__":
    print("Select mode:")
    print("1. Calculate optimal path based on distance")
    print("2. Calculate optimal path based on price")
    print("3. Calculate optimal path based on time")
    choice = input("Enter choice (1, 2, or 3): ").strip()

    if choice == '1':
        run_distance_program()
    elif choice == '2':
        run_price_program()
    elif choice == '3':
        run_time_program()
    else:
        print("Invalid choice")
