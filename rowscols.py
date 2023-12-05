MAX_ROWS = 10
MAX_COLS = 10


rows, cols = map(int, input("Enter the number of rows and columns: ").split())

if rows <= 0 or cols <= 0 or rows > MAX_ROWS or cols > MAX_COLS:
    print("Invalid input for matrix size.")

mat = [[0 for i in range(cols)] for j in range(rows)]

for i in range(rows):
    for j in range(cols):
        mat[i][j] = int(input("Enter element ({},{}): ".format(i, j)))

new_mat = [[0 for i in range(rows)] for j in range(cols)]
for i in range(rows):
    for j in range(cols):
        new_mat[j][i] = mat[i][j]

  # Print the matrix with the rows and columns swapped.
print("Matrix with rows and columns swapped:")
for i in range(cols):
    for j in range(rows):
        print(new_mat[i][j], end=" ")
    print()