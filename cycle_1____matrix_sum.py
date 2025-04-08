import numpy as np

def print_matrix(m):
    for row in m:
        for value in row:
            print(value, end=' ')
        print()

print("Matrix : 1")
r1 = int(input("Enter the number of rows: "))
c1 = int(input("Enter the number of columns: "))
m1 = np.zeros((r1, c1), dtype=int)
for i in range(r1):
    for j in range(c1):
        m1[i][j] = int(input(f"Enter the element ({i+1}, {j+1}): "))

print("Matrix : 2")
r2 = int(input("Enter the number of rows: "))
c2 = int(input("Enter the number of columns: "))
m2 = np.zeros((r2, c2), dtype=int)
for i in range(r2):
    for j in range(c2):
        m2[i][j] = int(input(f"Enter the element ({i+1}, {j+1}): "))

if r1 == r2 and c1 == c2:
    res = np.zeros((r1, c1), dtype=int)
    for i in range(r1):
        for j in range(c1):
            res[i][j] = m1[i][j] + m2[i][j]
    print("Resultant Matrix:")
    print_matrix(res)
else:
    print("Matrix addition is not possible.")
