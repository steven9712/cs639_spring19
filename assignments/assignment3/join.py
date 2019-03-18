import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(orders):
    # YOUR CODE GOES HERE
    key = orders[1]
    value = list(orders)
    mr.emit_intermediate(key, value)
    

# Implement the REDUCE function
def reducer(key, value):
    # YOUR CODE GOES HERE
    for i in range(1, len(value)):
        mr.emit((value[0] + value[i]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
