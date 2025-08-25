import itertools

def dummy_traveling_salesman(cities, distance_matrix):
    """
    Solves the Traveling Salesman Problem using brute-force (dummy implementation).
    
    Args:
        cities (list): List of city names or indices.
        distance_matrix (list of lists): 2D matrix where distance_matrix[i][j] is the distance from city i to city j.
    
    Returns:
        tuple: (best_route, min_distance)
    """
    n = len(cities)
    min_distance = float('inf')
    best_route = None

    # Generate all possible routes (permutations)
    for perm in itertools.permutations(range(n)):
        # Calculate total distance for this route (returning to start)
        distance = 0
        for i in range(n):
            distance += distance_matrix[perm[i]][perm[(i+1)%n]]
        if distance < min_distance:
            min_distance = distance
            best_route = perm

    # Convert indices to city names if needed
    best_route_names = [cities[i] for i in best_route]
    return best_route_names, min_distance

# Example usage
if __name__ == "__main__":
    cities = ['A', 'B', 'C', 'D']
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    route, distance = dummy_traveling_salesman(cities, distance_matrix)
    print(f"Best route: {route}")
    print(f"Minimum distance: {distance}")