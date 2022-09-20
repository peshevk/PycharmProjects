rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

sum_elements = 0

for row in range(rows):
    for col in range(cols):
        sum_elements += matrix[row][col]

print(sum_elements)
print(matrix)
