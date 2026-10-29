Here is the complete documentation and implementation based on your requirements.

---

### ## Problem Statement

Design a program that automatically generates a seating grid for a classroom or hall given the number of rows, columns, student capacity, and a list of reserved seats. Students should be assigned seats in an alternating checkerboard pattern where the sum of the row and column indices is even `(r + c) % 2 == 0`, while skipping reserved seats marked with `"X"`. Unassigned empty seats remain `"_"`.

---

### ## Algorithm

1. **Initialize Grid:** Create a 2D list of dimensions `rows` $\times$ `cols`, with all positions initialized to `"_"`.
2. **Mark Reserved Seats:** Iterate through the given `reserved` coordinate tuples and place `"X"` at those positions in the grid (ensuring coordinates are within bounds).
3. **Assign Students:**
* Initialize `student_count` to 1.
* Loop through each row `r` and column `c` in the grid.
* Check if the cell is empty (`"_"`) and satisfies the checkerboard condition `(r + c) % 2 == 0`.
* If the capacity limit (`student_count <= capacity`) is not yet reached, assign the student label (e.g., `"S01"`, `"S02"`) and increment `student_count`.


4. **Display Grid:** Print the final grid along with column (`C0`, `C1`...) and row (`R0`, `R1`...) headers.

---

### ## Flowchart

```mermaid
flowchart TD
    A[Start: generate_seating] --> B[Initialize grid with '_']
    B --> C[Mark reserved seats with 'X']
    C --> D[Set student_count = 1]
    D --> E{For each row r}
    E --> F{For each column c}
    F --> G{Is grid[r][c] == '_'?}
    G -- Yes --> H{Is (r + c) % 2 == 0?}
    G -- No --> L[Next Cell]
    H -- Yes --> I{Is student_count <= capacity?}
    H -- No --> L
    I -- Yes --> J[Assign Sxx to grid[r][c] & increment student_count]
    I -- No --> L
    J --> L
    L --> F
    F --> E
    E --> M[Return grid]
    M --> N[Print grid & End]

```

---

### ## Python Source Code

```python
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

```

---

### ## Sample Input

```python
rows = 4
cols = 4
capacity = 6
reserved = [(0, 1), (2, 2)]

```

---

### ## Sample Output

```text
     C0   C1   C2   C3
--------------------------
R0 | S01  X    S02  _
R1 | _    S03  _    S04
R2 | S05  _    X    _
R3 | _    S06  _    _

```
