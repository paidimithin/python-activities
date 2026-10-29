def generate_seating(rows, cols, capacity, reserved):
    grid = [["_" for _ in range(cols)] for _ in range(rows)]
    
    for r, c in reserved:
        if 0 <= r < rows and 0 <= c < cols:
            grid[r][c] = "X"
    
    student_count = 1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "_":
                if (r + c) % 2 == 0:
                    if student_count <= capacity:
                        grid[r][c] = f"S{student_count:02d}"
                        student_count += 1
                        
    return grid

def print_grid(grid):
    cols = len(grid[0])
    print("     " + "   ".join([f"C{c}" for c in range(cols)]))
    print("-" * (6 + cols * 5))
    for r, row in enumerate(grid):
        print(f"R{r} | " + "  ".join(row))

rows = 4
cols = 4
capacity = 6
reserved = [(0, 1), (2, 2)]

seating_arrangement = generate_seating(rows, cols, capacity, reserved)
print_grid(seating_arrangement)
