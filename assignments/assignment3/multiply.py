import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(matrix):
    # YOUR CODE GOES HERE
    if matrix[0] == 'a':
        for i in range(5):
            key = (matrix[1], i)
            mr.emit_intermediate(key, matrix)

    if matrix[0] == 'b':
        for j in range(5):
            key = (j, matrix[2])
            mr.emit_intermediate(key, matrix)

# Implement the REDUCE function
def reducer(key, value):
    # YOUR CODE GOES HERE
    matrix_a = [0] * 5
    matrix_b = [0] * 5
    product = 0
    row = list(key)
    for i in value:
        if i[0] == 'a':
            matrix_a[i[2]] = i[3]
        if i[0] == 'b':
            matrix_b[i[1]] = i[3]

    
    for j in range(5):
        product += matrix_a[j] * matrix_b[j]
    row.append(product)
    row = tuple(row)
    mr.emit((row))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
