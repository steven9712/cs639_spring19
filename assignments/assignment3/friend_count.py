import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(friends):
    friend1 = friends[0]
    friend2 = friends[1]
    mr.emit_intermediate(friend1, 1)
    

# Implement the REDUCE function
def reducer(key, value):
    # YOUR CODE GOES HERE
    mr.emit((key, sum(value)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
