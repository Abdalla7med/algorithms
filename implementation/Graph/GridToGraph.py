def grid_to_adjacency_matrix(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Initialize an empty adjacency matrix
    adjacency_matrix = [[0 for _ in range(rows * cols)] for _ in range(rows * cols)]

    # Helper function to get neighbors of a cell
    def get_neighbors(row, col):
        neighbors = []
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                neighbors.append((new_row, new_col))
        return neighbors

    # Populate adjacency matrix
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                current_node = row * cols + col
                neighbors = get_neighbors(row, col)
                for neighbor_row, neighbor_col in neighbors:
                    neighbor_node = neighbor_row * cols + neighbor_col
                    adjacency_matrix[current_node][neighbor_node] = 1

    return adjacency_matrix

# Example grid
grid = [
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 0]
]

# Convert grid to adjacency matrix
adjacency_matrix = grid_to_adjacency_matrix(grid)

# Print adjacency matrix
for row in adjacency_matrix:
    print(row)
